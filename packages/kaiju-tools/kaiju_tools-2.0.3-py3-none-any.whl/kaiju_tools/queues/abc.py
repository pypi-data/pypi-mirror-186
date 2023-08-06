import abc
import asyncio

from kaiju_tools.services import ContextableService

__all__ = ['BaseParallelJobsService', 'QueueServiceInterface', 'QueueService']


class QueueServiceInterface(abc.ABC):
    """An interface for queue classes."""

    @abc.abstractmethod
    async def put(self, value):
        """Should be used to put a value to the queue."""

    @abc.abstractmethod
    async def put_many(self, values):
        """Should be used to put a list of values to the queue."""


class BaseParallelJobsService(ContextableService, abc.ABC):
    """
    Base class for all services with parallel asynchronous jobs (workers) and
    jobs scaling.
    """

    class _Worker:
        """Job worker."""

        __slots__ = ('task', 'enabled', 'waiting')

        def __init__(self, f, enabled: bool = True):
            self.task = asyncio.create_task(f(self))
            self.enabled = enabled
            self.waiting = asyncio.Event()

        def __repr__(self):
            return f'<Worker>[done: {self.task.done()}, enabled: {self.enabled} waiting: {self.waiting.is_set()}]'

    MIN_PARALLEL_JOBS = 2
    MAX_PARALLEL_JOBS = 16
    DAEMON_REFRESH_RATE = 20.0

    def __init__(
            self, app,
            min_parallel_jobs: int = MIN_PARALLEL_JOBS,
            max_parallel_jobs: int = MAX_PARALLEL_JOBS,
            daemon_refresh_rate: float = DAEMON_REFRESH_RATE,
            logger=None
    ):
        """
        :param app:
        :param min_parallel_jobs:
        :param max_parallel_jobs:
        :param daemon_refresh_rate: in seconds, 0 for no daemon process and no scaling
        :param logger:
        """
        ContextableService.__init__(self, app=app, logger=logger)
        self._max_parallel_jobs = max(1, int(max_parallel_jobs))
        self._min_parallel_jobs = min(max(1, int(min_parallel_jobs)), self._max_parallel_jobs)
        self._daemon_refresh_rate = float(daemon_refresh_rate)
        self._daemon_task = None
        self._workers = None
        self._running = asyncio.Event()
        self._closing = False

    async def init(self):
        self._closing = False
        self._running.set()
        self._workers = []
        for _ in range(self._min_parallel_jobs):
            self._create_worker()
        self._daemon_task = asyncio.create_task(self._daemon())

    async def close(self):
        if not self.closed:
            self._closing = True
            self._running.clear()
            if not self._daemon_task.done():
                self._daemon_task.cancel()
            await asyncio.gather(*(self._cancel_worker(w) for w in self._workers))
            self._daemon_task = None
            self._workers = None

    async def pause(self):
        self._running.clear()
        await asyncio.gather(*(worker.waiting.wait() for worker in self._workers))

    def unpause(self):
        self._running.set()

    @property
    def closed(self) -> bool:
        return not self._workers

    def _create_worker(self):
        worker = self._Worker(self._worker)
        self._workers.append(worker)

    @staticmethod
    async def _cancel_worker(worker):
        if not worker.task.done():
            await worker.waiting.wait()
            worker.task.cancel()

    @abc.abstractmethod
    async def _worker(self, worker: _Worker):
        """
        Here you should define your worker loop.

        You should use worker object conditions to ensure that the worker task
        won't be cancelled while it is performing a useful operation.

        worker.enabled - False means that worker is expected to be cancelled
            use it as condition for a while loop

        worker.waiting - set this event each time the worker waits for something
        to happen (reading from a remote queue for example), this flag means
        that the daemon is allowed to cancel the worker immediately. Unset this
        when the worker performs a sensitive operation.

        self._running - you should wait for this event inside a wait phase
        to be able to pause workers
        """

        await self._running.wait()

        while worker.enabled:

            worker.waiting.set()

            if not self._running.is_set() and not self._closing:
                await self._running.wait()

            # do stuff here like receiving data from somewhere (without committing yet)

            worker.waiting.clear()

            # do all calculations / operations / commits for a single data element

    def _determine_scaling(self) -> int:
        """
        This method should determine whether number of workers should increase/decrease
        or remain constant based on some conditions. Return 0 for no scaling,
        positive value for positive scaling and negative for negative.

        .. note::

            A number of workers can't exceed the limits defined on a class init
            (min_jobs, max_jobs settings). Thus a number returned by this method
            is checked against the conditions in the daemon function.

        """

        return 0

    async def _routine(self):
        """Here you may define a custom periodic operation which daemon will
        perform each cycle after the scaling."""

    async def _daemon(self):
        """Daemon task is used to reschedule or scale workers in background."""

        if not self._daemon_refresh_rate:
            return

        while self._running.is_set():

            await asyncio.sleep(self._daemon_refresh_rate)

            self._workers = [w for w in self._workers if not w.task.done()]
            workers_num = len(self._workers)
            scale = self._determine_scaling()
            workers_expected = min(max(workers_num + scale, self._min_parallel_jobs), self._max_parallel_jobs)
            scale = workers_expected - workers_num
            # self.logger.debug('workers: %d, scale: %d', workers_num, scale)
            # self.logger.debug(self._workers)
            if scale > 0:
                # self.logger.debug('Adding new workers.')
                for _ in range(scale):
                    self._create_worker()
            elif scale < 0:
                # self.logger.debug('Removing idle workers.')
                for worker in self._workers[scale:]:
                    worker.enabled = False
                    if worker.waiting.is_set():
                        worker.task.cancel()

            await self._routine()


class QueueService(QueueServiceInterface, BaseParallelJobsService, abc.ABC):
    """
    A simple asyncio queue service with parallel workers and safe joins.
    """
    queue_class = asyncio.Queue             #: used to init the queue
    RAISE_EXCEPTION = False
    MIN_PARALLEL_JOBS = 1
    MAX_PARALLEL_JOBS = BaseParallelJobsService.MAX_PARALLEL_JOBS
    MAX_BATCH_SIZE = 100
    MULTIPLIER = MAX_BATCH_SIZE * 4
    MIN_BATCH_SIZE = 1
    DAEMON_REFRESH_RATE = BaseParallelJobsService.DAEMON_REFRESH_RATE

    def __init__(
            self, app,
            max_queue_size: int = None,
            min_parallel_jobs: int = MIN_PARALLEL_JOBS,
            max_parallel_jobs: int = MAX_PARALLEL_JOBS,
            min_batch_size: int = MIN_BATCH_SIZE,
            max_batch_size: int = MAX_BATCH_SIZE,
            daemon_refresh_rate: float = DAEMON_REFRESH_RATE,
            raise_exception: bool = RAISE_EXCEPTION,
            logger=None
    ):
        """
        :param app:
        :param max_queue_size: asyncio queue size
        :param min_parallel_jobs: min number of parallel asyncio workers
        :param max_parallel_jobs: max number of parallel asyncio workers
        :param min_batch_size:
        :param max_batch_size:
        :param daemon_refresh_rate: refresh rate for jobs daemon
        :param raise_exception: False will suppress exceptions in a worker loop
        :param logger:
        """
        BaseParallelJobsService.__init__(
            self, app=app, min_parallel_jobs=min_parallel_jobs,
            daemon_refresh_rate=daemon_refresh_rate,
            max_parallel_jobs=max_parallel_jobs, logger=logger)

        if max_queue_size is None:
            self._max_queue_size = self._max_parallel_jobs * self.MULTIPLIER
        else:
            self._max_queue_size = max(self._max_parallel_jobs, int(max_queue_size))
        self._raise_exception = bool(raise_exception)
        self._max_batch_size = max(1, int(max_batch_size))
        self._min_batch_size = min(self._max_batch_size, max(1, int(min_batch_size)))
        self._needs_scaling = False
        self._needs_removing = False
        self._queue = None

    @abc.abstractmethod
    async def process_batch(self, values):
        """Here you can write your own custom logic of batch processing."""

    async def init(self):
        self._needs_scaling = False
        self._queue = self.queue_class(maxsize=self._max_queue_size)
        await super().init()

    @property
    def closed(self) -> bool:
        return self._queue is None

    async def close(self):
        if not self.closed:
            self._closing = True
            self._running.clear()
            await self._queue.join()
            await super().close()
            self._queue = None

    async def put(self, value):
        """Acts like a normal queue.put."""

        if not self._running.is_set():
            await self._running.wait()
        if not self._queue.full():
            self._queue.put_nowait(value)
        else:
            await self._queue.put(value)

    async def put_many(self, values):
        """Acts like a normal queue.put but you can pass multiple values at once."""

        if not self._running.is_set():
            await self._running.wait()
        free_space = self._max_queue_size - self._queue.qsize()
        for value in values:
            if free_space:
                self._queue.put_nowait(value)
                free_space -= 1
            else:
                if not self._running.is_set():
                    await self._running.wait()
                await self._queue.put(value)
                free_space = self._max_queue_size - self._queue.qsize()

    def _determine_scaling(self) -> int:
        """
        Very simple scaling function. If the queue is full two daemon cycles
        in a row then add 1 more worker. Otherwise don't do anything.
        (same for downscaling but it has a little less priority than upscale)
        """

        # self.logger.debug(
        #     'Queue %s; needs_scaling: %d needs_removing: %d',
        #     self._queue, self._needs_scaling, self._needs_removing)

        if self._queue.full():
            if self._needs_scaling:
                self._needs_scaling = False
                return 1
            else:
                self._needs_scaling = True
                self._needs_removing = False
        elif self._queue.empty():
            if self._needs_scaling:
                self._needs_scaling = False
            elif self._needs_removing:
                self._needs_removing = False
                return -1
            else:
                self._needs_removing = True
        else:
            self._needs_scaling = False
            self._needs_removing = False

        return 0

    async def _receive_batch(self) -> list:
        """Receives a batch of values from the queue."""

        values = []

        if not self._queue.empty():
            for _ in range(min(self._max_batch_size, self._queue.qsize())):
                values.append(self._queue.get_nowait())
        else:
            while len(values) < self._min_batch_size:
                value = await self._queue.get()
                values.append(value)

        return values

    async def commit(self, values, results):
        """Commits the results."""
        for _ in range(len(values)):
            self._queue.task_done()

    async def on_exception(self, values, exc):
        """Here you can write your own custom logic of exception handling."""
        self.logger.error(
            'An error in the queue worker loop (worker error): %s', exc,
            exc_info=(type(exc), exc, exc.__traceback__))
        await self.commit(values, exc)

    async def _worker(self, worker):

        await self._running.wait()

        while worker.enabled:

            worker.waiting.set()
            if not self._running.is_set() and not self._closing:
                await self._running.wait()
            values = await self._receive_batch()
            worker.waiting.clear()

            try:
                results = await self.process_batch(values)
            except Exception as exc:
                await self.on_exception(values, exc)
                if self._raise_exception:
                    raise
            else:
                await self.commit(values, results)
