"""
Pytest fixtures. They can be used in your tests.

Fixtures
--------

"""

import gc
import logging
import multiprocessing as mp
import os
import platform
import queue
import signal
import traceback
import uuid
from datetime import timedelta, datetime
from inspect import iscoroutinefunction
from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile
from time import sleep
from types import SimpleNamespace

import pytest

__all__ = (
    'logger', 'application', 'run_in_process', 'performance_test', 'system_information',
    'temp_dir', 'sample_file'
)


@pytest.fixture(scope='session')
def system_information():
    """Used in tests for printing."""

    t = datetime.now().strftime('%Y-%m-%d %H:%M')
    _sys = platform.version()
    _python = platform.python_version()

    return f"""Python {_python}
{_sys}
{t}
"""


@pytest.fixture(scope='session')
def logger():
    """
    Returns a test logger preconfigured to DEBUG level. You may use it in tests
    or in your services as the base logger.
    """

    logger = logging.getLogger('pytest')
    logger.setLevel('DEBUG')
    return logger


@pytest.fixture
def application():
    """
    Returns a sample aiohttp web app object to use in tests. Requires aiohttp.

    You may pass a list of `Service` classes. They won't be initialized but they will be registered
    in the pseudo-service context meaning you can use `app.services.<service_name>` inside you code
    as if it's a normal initialized app.
    """
    from aiohttp.web import Application

    def _application(*services, name='pytest', id=str(uuid.uuid4())):
        app = Application(logger=logger)
        app['id'] = app.id = id
        app['name'] = app.name = name
        app['env'] = app.env = 'dev'
        app.services = SimpleNamespace(**{service.service_name: service for service in services})
        return app

    return _application


@pytest.fixture
def temp_dir():
    with TemporaryDirectory(prefix='pytest') as d:
        yield Path(d)


@pytest.fixture
def sample_file():
    with NamedTemporaryFile(prefix='pytest', delete=False) as f:
        name = f.name
        f.write('test')
    yield Path(name)
    os.remove(name)


@pytest.fixture
def run_in_process():
    """
    Runs an async function in a separate process. This function will return
    the result of a process execution or raise an exception.

    .. code-block:: python

        async def my_function(a, b, c):
            await asyncio.sleep(42)
            return b * c

        result = run_in_process_async(my_function, args=(5, 6, 7))  # returns 42


    :param func: a function to run
    :param timeout: timeout in sec, after reaching it a `os.kill` with a
        specified signal will be cast on a process holding the function
        if timeout is None, then the executor will wait until process is
        finished
    :param signal_type: signal type to use with `os.kill`, if None was
        provided
    :param args: positional arguments to pass to the user's function
    :return:

    """

    import uvloop

    def _run_in_process(
            func, timeout: int = None, signal_type=signal.SIGINT,
            args: tuple = None):

        def _process(error_queue, result_queue, f, args):
            try:
                if iscoroutinefunction(f):
                    loop = uvloop.new_event_loop()
                    # loop = asyncio.new_event_loop()
                    result = loop.run_until_complete(f(*args))
                else:
                    result = f(*args)
            except Exception as err:
                traceback.print_tb(err.__traceback__)
                error_queue.put_nowait(err)
            else:
                result_queue.put_nowait(result)

        errors, results = mp.Queue(), mp.Queue()
        if args is None:
            args = tuple()
        proc = mp.Process(target=_process, args=(errors, results, func, args))
        proc.start()
        if timeout and signal_type is not None:
            sleep(timeout)
            os.kill(proc.pid, signal_type)
        else:
            proc.join(timeout=timeout)
        try:
            raise errors.get_nowait()
        except queue.Empty:
            pass
        try:
            return results.get_nowait()
        except queue.Empty:
            return

    return _run_in_process


@pytest.fixture
def performance_test(run_in_process):
    """
    This is a performance tester fixture. You can use it to test your
    function for performance.

    How to use:

    The function you test must return a float timedelta value and a total number
    of events. A simplest example is shown below.

    .. code-block:: python

        async def func_you_need_to_test(count, other_arg):
            counter = 0
            t0 = time()
            for _ in range(counter):
                ... # do something
                if success:
                    counter += 1
            t1 = time()
            return t1 - t0, counter

        dt, counter, rps = performance_test(func_you_need_to_test, (1000, 'something',))


    .. note::

        The function will run in a separate process and in a separate asyncio
        loop (if it's an async), so you shouldn't use any variable from an
        outer scope in it. You have to provide all arguments you need to
        a *performance_test* call.

    The tester will perform a few runs in an isolated process and will return
    a timedelta object (time taken), total counter and RPS.

    :param f: function to test, must return timedelta and a performance value
    :param args: function args
    :param runs: number of runs
    :param timeout: timeout in seconds for a function run
    :param run_in_separate_process: perform a test in a separate process
    :returns: a timedelta, total event counter and RPS
    """

    import uvloop

    def _performance_test(f, args: tuple, runs=3, timeout=60, run_in_separate_process=False):

        def _wrapper_function(f, args):
            gc.collect()
            gc.disable()
            result = f(*args)
            if iscoroutinefunction(f):
                # loop = asyncio.new_event_loop()
                loop = uvloop.new_event_loop()
                result = loop.run_until_complete(result)
            gc.enable()
            return result

        runs = max(1, runs)
        _dt, _counter = None, None

        for run in range(runs + 1):
            if run_in_separate_process:
                dt, counter = run_in_process(
                    _wrapper_function, timeout, signal_type=None, args=(f, args))
            else:
                dt, counter = _wrapper_function(f, args)
            if not _dt or dt < _dt:
                _dt = dt
                _counter = counter

        if not _counter:
            raise ValueError('No counter returned.')

        _speed = round(_counter / _dt, 1)
        _dt = timedelta(seconds=_dt)

        return _dt, _counter, _speed

    return _performance_test
