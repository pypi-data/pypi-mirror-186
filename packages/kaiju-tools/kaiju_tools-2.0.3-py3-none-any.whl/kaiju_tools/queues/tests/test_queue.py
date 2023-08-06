import asyncio

from .fixtures import *


@pytest.mark.asyncio
async def test_queue_basic_operation(queue):
    SIZE = 10000
    await queue.put_many(list(range(SIZE)))
    await queue.close()
    assert len(queue.values) == SIZE
    assert not queue.errors


@pytest.mark.asyncio
async def test_queue_on_close(queue):
    await queue.close()
    task = asyncio.create_task(queue.put(1))
    await asyncio.sleep(0.1)
    await queue.init()
    await task  # the task should proceed normally
    await queue.close()
    assert queue.values[0], 'the task value should be processed by the queue'


@pytest.mark.asyncio
async def test_queue_on_pause(queue):
    SIZE = 10000
    await queue.pause()
    task = queue.put_many(list(range(SIZE)))
    task = asyncio.create_task(task)
    await asyncio.sleep(0.1)
    assert not queue.errors, 'on pause the queue should not process any messages'
    assert not queue.values, 'on pause the queue should not process any messages'
    queue.unpause()
    await task  # the task should proceed normally
    await queue.close()
    assert len(queue.values) == SIZE


@pytest.mark.asyncio
async def test_queue_error_handling(queue):
    await queue.put('not_number')
    await queue.close()
    assert not queue.values, 'error hook should be used for invalid data'
    assert queue.errors, 'error hook should be used for invalid data'
