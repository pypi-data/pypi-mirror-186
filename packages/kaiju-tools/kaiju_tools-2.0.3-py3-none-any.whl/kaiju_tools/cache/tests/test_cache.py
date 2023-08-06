import asyncio
import uuid

import pytest

from ..services import *

__all__ = ['cache_service_test']


async def cache_service_test(cache, logger):

    logger.info("Testing basic operations")

    async with cache:

        key = str(uuid.uuid4())
        await cache.set(key, key, ttl=10, nowait=False)
        _value = await cache.get(key)
        assert _value == key
        await cache.delete(key, nowait=False)
        _value = await cache.exists(key)
        assert _value is False

        logger.info("Testing bulk operations")

        key1, key2 = str(uuid.uuid4()), str(uuid.uuid4())

        await cache.m_set({key1: key1, key2: key2}, nowait=False)
        values = await cache.m_exists([key1, key2])
        assert key1 in values
        assert key2 in values

        values = await cache.m_get([key1, key2, 'key3'])
        assert values[key1] == key1
        assert values[key2] == key2
        assert 'key3' not in values

        await cache.m_delete([key1, key2], nowait=False)
        values = await cache.m_exists([key1, key2])
        assert key1 not in values
        assert key2 not in values

        await cache.m_set({key1: key1, key2: key2}, ttl=10, nowait=False)
        values = await cache.m_get([key1, key2])
        assert values[key1] == key1
        assert values[key2] == key2

        logger.info("Testing json dumps")

        await cache.set(key, {'data': True}, nowait=False)
        result = await cache.get(key)
        assert result['data'] is True

        logger.info("Testing nowait operations")

        nowait_key_1, nowait_key_2 = 'nowait_key_1', 'nowait_key_2'
        await cache.m_set({nowait_key_1: nowait_key_1, nowait_key_2: nowait_key_2}, ttl=10, nowait=True)
        await cache.delete(nowait_key_1, nowait=True)

        await asyncio.sleep(0.1)  #: giving background tasks a chance to execute

        nowait_key_cached = await cache.get(nowait_key_2)
        assert nowait_key_cached == nowait_key_2, "nowait key should be set in background"
        nowait_key_exists = await cache.exists(nowait_key_1)
        assert not nowait_key_exists, "nowait key should be removed in background"


@pytest.mark.asyncio
async def test_local_cache(logger):
    cache = LocalCacheService(app=None, logger=logger)
    await cache_service_test(cache, logger=logger)
