from typing import Optional

from kaiju_tools.services import ContextableService
from kaiju_tools.ttl_dict import TTLDict

from .abc import BaseCacheService, CacheServiceInterface

__all__ = ['LocalCacheService']


class LocalCacheService(ContextableService, CacheServiceInterface):
    """
    Local cache an adapter between thee cache interface and a TTLDict class.

    Most of configuration parameters are not used and left only for the
    sake of compatibility.

    You can use this as in-memory cache if you have only a single app instance
    or in case you need a mock cache service for your tests.

    :param app:
    :param default_ttl:  default key lifetime in seconds (0 for infinite)
    """

    DEFAULT_TTL = BaseCacheService.DEFAULT_TTL
    TTL_CLASS = TTLDict

    def __init__(self, app, transport=False, namespace=None, default_ttl: int = DEFAULT_TTL, logger=None, **kws):
        super().__init__(app=app, logger=logger)
        self._default_ttl = max(self.DEFAULT_TTL, int(default_ttl))
        self._dict = self.TTL_CLASS()
        self._dict.set_ttl(self._default_ttl)

    async def exists(self, key: str, ignore_conn_errors=None) -> bool:
        return key in self._dict

    async def m_exists(self, keys: str, ignore_conn_errors=None) -> frozenset:
        return frozenset(key for key in keys if key in self._dict)

    async def get(self, key: str, use_serializer=None, ignore_conn_errors=None):
        return self._dict.get(key)

    async def m_get(self, keys: str, use_serializer=None, ignore_conn_errors=None) -> dict:
        return {key: self._dict.get(key) for key in keys if key in self._dict}

    async def set(self, key: str, value, ttl: int = None, use_serializer=None, ignore_conn_errors=None, nowait=None):
        if ttl is None:
            ttl = self._default_ttl
        return self._dict.set(key, value, ttl=ttl)

    async def m_set(self, keys: dict, ttl: int = None, use_serializer=None, ignore_conn_errors=None, nowait=None):
        if ttl is None:
            ttl = self._default_ttl
        for key, value in keys.items():
            self._dict.set(key, value, ttl=ttl)

    async def delete(self, key: str, ignore_conn_errors=None, nowait=None):
        del self._dict[key]

    async def m_delete(self, keys: str, ignore_conn_errors=None, nowait=None):
        for key in keys:
            del self._dict[key]
