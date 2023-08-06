import abc
from asyncio import Queue, ensure_future, sleep, gather
from itertools import chain
from typing import *

from aiohttp import ClientConnectionError

from .schema import Index
from .client import ESService, BulkError
from ..services import Service

__all__ = ['ESLoaderService']


class ESLoaderService(Service, abc.ABC):
    """A simple queue based ES data loader."""

    service_name = 'es_loader'

    DEFAULT_SENDERS = 5
    MAX_SENDERS = 64
    MAX_BATCH_SIZE = 10000
    DEFAULT_BATCH_SIZE = 500

    _performance_settings = {
        'index': {
            'refresh_interval': -1,
            'number_of_replicas': 0
        }
    }

    def __init__(
            self, app, indices: Collection[Index],
            generator: AsyncGenerator[Tuple[Index, dict], None],
            es_service_name: str = ESService.service_name,
            senders=DEFAULT_SENDERS, sender_batch_size=DEFAULT_BATCH_SIZE,
            logger=None):
        """
        :param app: aiohttp web app with a registered ESService
        :param indices: a collection of indices
        :param generator: an async generator object returning row by row
            (Index, doc) pairs for the loader, when loader finishes, the generator
            also must exit
        :param es_service_name: optional ES service name for service discovery
        :param senders: number of parallel workers
        :param sender_batch_size: max number of docs in each request
        :param logger:
        """

        super().__init__(app=app, logger=logger)
        self._es = self.app[es_service_name]

        self._indices = tuple(indices)
        self._generator = generator
        self._number_of_senders = min(max(int(senders), 1), self.MAX_SENDERS)
        self._sender_batch_size = min(max(int(sender_batch_size), 1), self.MAX_BATCH_SIZE)

        self._senders = []
        self._closing = False

    def __await__(self):
        return self._run()

    async def _run(self):
        """Start the loading process."""

        logger = self.logger

        logger.debug('Updating indices settings for maximum loading performance.')

        indices = self._indices
        settings = [
            {
                'refresh_interval': index.settings['index']['refresh_interval'],
                'number_of_replicas': index.settings['index']['number_of_replicas']
            }
            for index in self._indices
        ]

        await gather(*(
            self._es.update_index_settings(idx, self._performance_settings)
            for idx in indices
        ))

        queues = {
            index.alias: Queue(maxsize=self._number_of_senders * self._sender_batch_size)
            for index in indices
        }

        logger.debug('Starting workers.')

        self.__senders = list(chain(*(
            [
                ensure_future(self._send(queues[index.alias], index))
                for _ in range(self._number_of_senders)
            ]
            for index in indices)))

        logger.debug('Loading data.')

        try:
            async for idx, doc in self._generator:
                await queues[idx.alias].put(doc)
        except Exception as e:
            logger.error(
                '[%s]: %s in parser. Terminating.',
                e.__class__.__name__, str(e))
            raise e
        else:
            await sleep(0.1)
            logger.debug('Joining queues.')
            self._closing = True
            await gather(*(queue.join() for queue in queues.values()))
        finally:
            await sleep(0.1)
            logger.debug('Refreshing indices.')
            await gather(*(self._es.refresh(idx) for idx in indices))
            logger.debug('Refreshing indices settings.')
            await gather(*(
                self._es.update_index_settings(idx, settings)
                for idx, settings in zip(indices, settings)
            ))
            logger.debug('Merging shards.')
            await gather(*(self._es.forcemerge(idx) for idx in indices))
            logger.debug('Deleting queues.')
            del queues
            logger.info('Finished loading.')

    async def _send(self, queue: Queue, index: Index):
        """Sender worker (assembles batches of data and sends it to ES)."""

        logger = self.logger
        es = self._es
        batch = []
        sender_batch_size = self._sender_batch_size
        errors = (TimeoutError, ConnectionError, ClientConnectionError)

        while 1:

            qsize = queue.qsize()
            if qsize:
                batch.extend((
                    queue.get_nowait()
                    for _ in range(min(qsize, sender_batch_size))))

            if self._closing:
                if not batch:
                    batch.append(await queue.get())
            else:
                if len(batch) < sender_batch_size:
                    await sleep(0.25)
                    continue

            try:
                await es.insert(index, batch)
            except errors as e:
                logger.error(
                    '[%s]: %s in sender. Retrying!',
                    e.__class__.__name__, str(e))
                await sleep(0.25)
                continue
            except BulkError as err:
                logger.error('A bulk error occurred. %s.', err.errors)
            except Exception as e:
                logger.error(
                    '[%s]: %s in sender. Skipping.',
                    e.__class__.__name__, str(e))

            for _ in batch:
                queue.task_done()
            batch = []
