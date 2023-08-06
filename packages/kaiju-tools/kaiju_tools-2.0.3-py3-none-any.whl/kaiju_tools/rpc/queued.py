import abc
import asyncio
import uuid
from collections import namedtuple
from typing import Union, List, Collection, Any, Optional

from . import jsonrpc
from ..services import ContextableService
from .server import JSONRPCServer
from .client import BaseRPCClientService

__all__ = (
    'AbstractQueuedRequestTransport', 'AbstractQueuedResponseTransport',
    'AbstractQueuedRequest',
    'QueuedRPCServer', 'SimpleQueuedRPCClientService'
)

AbstractQueuedRequest = namedtuple('AbstractQueuedRequest', 'headers data session callback_queue_id')


class AbstractQueuedRequestTransport(abc.ABC):

    @abc.abstractmethod
    async def init_queue(self, queue_id: str):
        pass

    @abc.abstractmethod
    async def get_callback_queue_id(self) -> str:
        pass

    @abc.abstractmethod
    async def get(self, queue_id: str) -> AbstractQueuedRequest:
        pass

    @abc.abstractmethod
    async def get_many(self, queue_id: str, max_num: int = None) -> Collection[AbstractQueuedRequest]:
        pass


class AbstractQueuedResponseTransport(abc.ABC):

    @abc.abstractmethod
    async def init_queue(self, queue_id: str):
        pass

    @abc.abstractmethod
    async def put(self, headers: dict, data: Union[dict, List[dict]], queue_id: str, callback_queue_id: Optional[str]):
        pass

    @abc.abstractmethod
    async def put_many(self, records: list):
        pass


class QueuedRPCServer(ContextableService):

    service_name = 'QueuedRPCServer'
    RESPONSE_QUEUE_SIZE = 1024
    REQUEST_WORKERS = 1
    RESPONSE_WORKERS = 1
    MAX_REQUEST_BATCH_SIZE = 256
    _CALLBACK_QUEUE_ID = '_callback_queue_id'

    def __init__(
        self, app,
        request_queue_id: str,
        rpc_server: Union[str, JSONRPCServer],
        requests_transport: Union[str, AbstractQueuedRequestTransport],
        responses_transport: Union[str, AbstractQueuedResponseTransport],
        response_queue_size: int = RESPONSE_QUEUE_SIZE,
        request_workers=REQUEST_WORKERS,
        response_workers=RESPONSE_WORKERS,
        max_request_batch_size=MAX_REQUEST_BATCH_SIZE,
        logger=None
    ):
        super().__init__(app=app, logger=logger)
        self._rpc_server = self.discover_service(rpc_server)
        self._request_transport = self.discover_service(requests_transport)
        self._response_transport = self.discover_service(responses_transport)

        self._response_queue_size = int(response_queue_size)
        self._request_queue_id = str(request_queue_id)
        self._request_workers = max(1, int(request_workers))
        self._response_workers = max(1, int(response_workers))
        self._max_request_batch_size = int(max_request_batch_size)

        self._closed = True
        self._response_queue = None
        self._response_worker_tasks = None
        self._request_worker_tasks = None

    async def init(self):
        self._response_queue = asyncio.Queue(maxsize=self._response_queue_size)
        self.logger.info('Initializing remote requests queue "%s".', self._request_queue_id)
        await self._request_transport.init_queue(queue_id=self._request_queue_id)
        self.logger.info('Starting workers.')
        self._request_worker_tasks = [
            asyncio.create_task(self._request_worker())
            for _ in range(self._request_workers)
        ]
        self._response_worker_tasks = [
            asyncio.create_task(self._response_worker())
            for _ in range(self._response_workers)
        ]
        self.logger.info('Started.')

    async def close(self):
        self._closed = True
        self.logger.info('Stopping request workers.')
        await asyncio.gather(self._request_worker_tasks)
        self.logger.info('Joining local response queue.')
        await self._response_queue.join()
        self.logger.info('Stopping response workers.')
        for task in self._response_worker_tasks:
            if not task.done():
                task.cancel()
        self.logger.info('Closed.')

    @property
    def closed(self) -> bool:
        return self._closed

    async def _request_worker(self):

        queue = self._rpc_server.requests
        callback = self._response_queue
        transport = self._request_transport
        queue_id = self._request_queue_id
        _CALLBACK_QUEUE_ID = self._CALLBACK_QUEUE_ID

        while not self._closed:

            requests = await transport.get_many(
                queue_id=queue_id, max_num=self._max_request_batch_size)
            size_left = queue.maxsize - queue.qsize()

            for headers, data, session, callback_queue_id in requests[:size_left]:
                headers[_CALLBACK_QUEUE_ID] = callback_queue_id
                queue.put_nowait((headers, data, session, callback))

            for headers, data, session, callback_queue_id in requests[size_left:]:
                headers[_CALLBACK_QUEUE_ID] = callback_queue_id
                await queue.put((headers, data, session, callback))

    async def _response_worker(self):

        queue = self._response_queue
        transport = self._response_transport
        _CALLBACK_QUEUE_ID = self._CALLBACK_QUEUE_ID

        while not self._closed and not queue.empty():

            if queue.empty():
                headers, data = await queue.get()
            else:
                headers, data = queue.get_nowait()

            callback_queue_id = headers.pop(_CALLBACK_QUEUE_ID, None)
            if callback_queue_id:
                await transport.put(headers, data, callback_queue_id, None)


async def response_callback_function_interface(headers: dict, data: Union[dict, List[dict]]):
    """Example of a response callback function."""


class SimpleQueuedRPCClientService(BaseRPCClientService):

    RETRIEVE_RESPONSES = True
    RESPONSE_WORKERS = 1
    RAISE_ON_ERROR = False
    MAX_RESPONSE_BATCH_SIZE = 512

    def __init__(
        self, app,
        requests_transport: Union[str, AbstractQueuedRequestTransport],
        callback_queue_id: str = None,
        token_service: Union[str, BaseRPCClientService.token_service_class] = False,
        responses_transport: Union[str, AbstractQueuedResponseTransport] = None,
        response_callback_function=None,
        response_workers=RESPONSE_WORKERS,
        max_response_batch_size=MAX_RESPONSE_BATCH_SIZE,
        raise_on_error=RAISE_ON_ERROR,
        logger=None
    ):

        self._request_transport = self.discover_service(requests_transport)
        callback_queue_id = str(callback_queue_id) if callback_queue_id else self._request_transport.get_callback_queue_id()
        super().__init__(app=app, uri=callback_queue_id, token_service=token_service, logger=logger)

        if response_callback_function:
            self._response_transport = self.discover_service(responses_transport)
        else:
            self._response_transport = None

        self.response_callback_function = response_callback_function
        self._response_workers = max(1, int(response_workers))
        self._max_response_batch_size = int(max_response_batch_size)
        self._raise_on_error = raise_on_error

        self._callback_queue_id = callback_queue_id
        self._response_worker_tasks = None
        self._closed = True

    async def init(self):
        self._closed = False
        if self.response_callback_function:
            self.logger.info('Initializing remote callback queue "%s".', self._callback_queue_id)
            await self._request_transport.init_queue(queue_id=self._callback_queue_id)
            self.logger.info('Starting workers.')
            self._response_worker_tasks = [
                asyncio.create_task(self._response_worker())
                for _ in range(self._response_workers)
            ]
        self.logger.info('Started.')

    async def close(self):
        self._closed = True
        if self.response_callback_function:
            self.logger.info('Joining local response queue.')
            self.logger.info('Stopping response workers.')
            for task in self._response_worker_tasks:
                if not task.done():
                    task.cancel()
        self.logger.info('Closed.')

    async def call(self, uri: str, method: str, params: Any = None, id=False, headers: dict = None):
        data = jsonrpc.RPCRequest(id, method, params)
        data = data.repr()
        headers = await self._set_headers(headers)
        headers[self.headers.CALLBACK_ID] = self._callback_queue_id
        await self._request_transport.put(headers, data, uri, self._callback_queue_id)

    async def _response_worker(self):

        transport = self._response_transport
        callback_function = self.response_callback_function
        raise_on_error = self._raise_on_error

        while not self._closed:

            responses = await transport.get_many(
                self._callback_queue_id, max_num=self._max_response_batch_size)
            results = await asyncio.gather(*(
                callback_function(*response)
                for response in responses
            ), return_exceptions=True)

            for result, response in zip(results, responses):
                if isinstance(result, Exception):
                    if raise_on_error:
                        raise result
                    else:
                        self.logger.error(
                            'Response processing error: "%s".'
                            ' Response: "%s".', result, response)
