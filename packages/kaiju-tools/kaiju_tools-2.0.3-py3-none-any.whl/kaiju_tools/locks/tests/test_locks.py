import asyncio
import pytest
import uuid

from ..abc import BaseLocksService
from ..exceptions import *

__all__ = ['locks_service_test']


async def locks_service_test(container, locks_service, logger):
    key = 'some_group:some_service'
    value = str(uuid.uuid4())

    logger.info('Initialization.')

    async with locks_service as locks:

        locks: BaseLocksService = locks

        logger.info('Testing basic locking.')

        await locks.acquire(key, value)
        owner = await locks.owner(key)
        assert owner == value
        await locks.release(key, value)

        logger.info('Testing locking/unlocking with ttl')

        await locks.acquire(key, value, ttl=1)
        await locks.acquire(key, value)

        logger.info('Testing waiting')

        with pytest.raises(LockAcquireTimeout):
            await locks.wait(key, timeout=0.001)

        logger.info('Trying to release a lock by a different owner should produce an error.')

        with pytest.raises(NotALockOwnerError):
            new_value = str(uuid.uuid4())
            await locks.release(key, new_value)

        logger.info('Trying to acquire an existing lock with wait=False should raise an error.')

        with pytest.raises(LockExistsError):
            await locks.acquire(key, new_value, wait=False)

        logger.info('Trying to set multiple locks at once (should raise an error for all except one)')

        results = await asyncio.gather(
            locks.acquire('key', str(uuid.uuid4()), wait=False),
            locks.acquire('key', str(uuid.uuid4()), wait=False),
            locks.acquire('key', str(uuid.uuid4()), wait=False),
            return_exceptions=True)

        counter = 0

        for value in results:
            logger.debug(value)
            if isinstance(value, LockExistsError):
                counter += 1

        assert counter == 2

        logger.info('Terminating.')
