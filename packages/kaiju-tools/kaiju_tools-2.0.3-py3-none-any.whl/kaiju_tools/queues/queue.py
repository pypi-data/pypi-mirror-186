import asyncio

from kaiju_tools.functions import retry
from .abc import QueueService

__all__ = ['ExecutorQueue']


class ExecutorQueue(QueueService):
    """
    A simple async executor queue capable of basic async operation.

    You can put an async function and its args tuple in the queue and it will perform
    a procedural call in the future.

    Expected `value` format in `put` methods:

        (<func>, <args>, <kws>, <callback>)

    func - async callable (function or method)
    args - list of positional args
    kws - list of kwargs
    callback - optional callback asyncio.Queue (set `None` for no callback)

    .. code-block:: python

        async def f(a):
            print(a)
            return 42

        queue = SimpleExecutorQueue(app, logger)
        await queue.put((f, ('Hello',), {}, None))  # will perform in the future
        cb = asyncio.Queue()
        await queue.put((f, (), {'a': 'Hi'}, cb) # with perform in the future and store result in cb queue

    """
    def __init__(self, *args, retry_settings: dict = None, **kws):
        """
        :param args: see `QueueService`
        :param retry_settings: settings for `retry` command, None for no retries
        :param kws: see `QueueService`
        """
        super().__init__(*args, **kws)
        self._retry_settings = retry_settings

    async def put(
        self, f, args: tuple = None, kws: dict = None, callback: asyncio.Queue = None, retry_kws: dict = None
    ):
        """
        Schedule execution of an async function in the executor.

        :param f: awaitable function
        :param args: function *args
        :param kws: function **kws
        :param callback: optional callback asyncio queue (the result will be put in there)
        :param retry_kws: you may specify retry() params here for the retry function (by default - do not use retry)
        """
        if args is None:
            args = tuple()
        if kws is None:
            kws = dict()
        await super().put((f, args, kws, callback, retry_kws))

    async def put_many(self, values: list):
        """
        Similar to `ExecutorQueue.put` but you can specify a list of function calls in one async call.

        :param values:
        """
        _values = []
        for value in values:
            f, args, kws, callback, retry_kws = [*value, *[None] * (5 - len(value))]
            if args is None:
                args = tuple()
            if kws is None:
                kws = dict()
            _values.append((f, args, kws, callback, retry_kws))
        await super().put_many(_values)

    async def process_batch(self, values) -> list:
        """
        Background operation (connected to the op queue). All it does is
        just runs the function with provided args. Thus each value in `values`
        is expected to be a (func, args) tuple. Returns the list of op results.

        Expected `value` format in `put` methods:

        (<func>, <args>, <kws>, <callback>)

        func - async callable (function or method)
        args - list of positional args
        kws - list of kwargs
        callback - optional callback asyncio.Queue (set `None` for no callback)
        """
        results = []

        for value in values:
            try:
                func, args, kws, callback, retry_kws = value
                if not retry_kws and self._retry_settings:
                    retry_kws = self._retry_settings
                if retry_kws:
                    result = await retry(func, args=args, kws=kws, **retry_kws)
                else:
                    result = await func(*args, **kws)
                if callback:
                    callback.put_nowait(result)
            except Exception as exc:
                result = exc
            results.append(result)

        return results
