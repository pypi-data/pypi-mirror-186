import pytest
import pytest_asyncio

from ..abc import QueueService


@pytest_asyncio.fixture
async def queue(logger):

    class CustomQueue(QueueService):

        def __init__(self, *args, **kws):
            super().__init__(*args, **kws)
            self.values = []
            self.errors = []

        async def process_batch(self, values):
            for value in values:
                self.values.append(value / 2)

        async def on_exception(self, values, exc):
            self.errors.append(exc)
            await self.commit(values, exc)

    queue = CustomQueue(None, daemon_refresh_rate=1, logger=logger)
    await queue.init()

    yield queue

    if not queue.closed:
        await queue.close()
