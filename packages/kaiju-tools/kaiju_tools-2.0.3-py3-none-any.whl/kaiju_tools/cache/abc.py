import abc
from typing import Union, Optional

from kaiju_tools.services import ContextableService, Service
from kaiju_tools.encoding.etc import MimeTypes
from kaiju_tools.encoding.serializers import serializers
from kaiju_tools.functions import RETRY_EXCEPTION_CLASSES
from kaiju_tools.rpc import AbstractRPCCompatible
from kaiju_tools.jsonschema import String, Generic, Object, Array, Boolean, Integer
from kaiju_tools.queues import ExecutorQueue

__all__ = ['CacheServiceInterface', 'BaseCacheService']


class CacheServiceInterface(abc.ABC):
    """Shared cache service public methods."""

    @abc.abstractmethod
    async def exists(self, key: str, ignore_conn_errors=False) -> bool:
        """Checks if key is present in the cache."""

    @abc.abstractmethod
    async def m_exists(self, keys: list, ignore_conn_errors=False) -> frozenset:
        """Returns a set of existing keys."""

    @abc.abstractmethod
    async def get(self, key: str, use_serializer=True, ignore_conn_errors=False) -> Optional:
        """Get value of a key or None if not found."""

    @abc.abstractmethod
    async def m_get(self, keys: list, use_serializer=True, ignore_conn_errors=False) -> dict:
        """Get value of multiple keys."""

    @abc.abstractmethod
    async def set(self, key: str, value, ttl: int = 0, use_serializer=True, ignore_conn_errors=False, nowait=True):
        """Set a single key at once."""

    @abc.abstractmethod
    async def m_set(self, keys: dict, ttl: int = 0, use_serializer=True, ignore_conn_errors=False, nowait=True):
        """Set one or multiple keys at once."""

    @abc.abstractmethod
    async def delete(self, key: str, ignore_conn_errors=False, nowait=True):
        """Remove one key at once."""

    @abc.abstractmethod
    async def m_delete(self, keys: list, ignore_conn_errors=False, nowait=True):
        """Remove multiple keys at once."""


class BaseCacheService(ContextableService, CacheServiceInterface, AbstractRPCCompatible, abc.ABC):
    """
    Base class for all shared cache services.

    Implements `CacheServiceInterface` interface.

    This is a base class. If you need to implement your own backend you have to
    program abstract methods:

    - `BaseCacheService._exists`
    - `BaseCacheService._m_exists`
    - `BaseCacheService._get`
    - `BaseCacheService._m_get`
    - `BaseCacheService._set`
    - `BaseCacheService._m_set`
    - `BaseCacheService._delete`
    - `BaseCacheService._m_delete`
    """

    DELIMITER = ':'     #: used for delimiting sections in a key
    CONNECTION_ERROR_CLASSES = RETRY_EXCEPTION_CLASSES

    # defaults

    DEFAULT_TTL = 0
    PREFIX = 'cache'
    DEFAULT_SERIALIZER_TYPE = MimeTypes.msgpack
    IGNORE_CONN_ERRORS = False
    NOWAIT = True
    MAX_QUEUE_SIZE = 128
    PARALLEL_JOBS = 1

    transport_cls = None

    def __init__(
        self, app, transport: Union[str, Service] = None, namespace: str = None,
        default_ttl: int = DEFAULT_TTL, serializer_type: str = DEFAULT_SERIALIZER_TYPE,
        queue_settings: dict = None, serializers=serializers, permissions=None,
        logger=None
    ):
        """
        :param app:
        :param namespace: optional namespace (by default == app.name)
        :param transport: transport service (may be Redis, DB or similar)
        :param default_ttl:  default key lifetime in seconds (0 for infinite)
        :param serializer_type: you may specify a serializer type from `kaiju-tools.encoding`
        :param serializers: serializers registry with all serializers classes
        :param queue_settings: you may pass custom background queue settings here (see `kaiju_tools.queue.QueueService`)
        :param permissions:
        :param logger:
        """
        Service.__init__(self, app=app, logger=logger)
        AbstractRPCCompatible.__init__(self, permissions=permissions)
        self._namespace = namespace if namespace else app['name']
        self._transport_name = transport
        self._default_ttl = max(self.DEFAULT_TTL, int(default_ttl))
        self._serializer = serializers[serializer_type]
        self._queue_settings = queue_settings if queue_settings else {}
        self._transport = None
        self._queue: ExecutorQueue = None

    @property
    def routes(self) -> dict:
        """RPC routes."""
        return {
            **super().routes,
            'exists': self.exists,
            'm_exists': self.m_exists,
            'get': self.get,
            'm_get': self.m_get,
            'set': self.set,
            'm_set': self.m_set,
            'delete': self.delete,
            'm_delete': self.m_delete
        }

    @property
    def permissions(self) -> dict:
        """RPC permissions."""
        return {
            self.DEFAULT_PERMISSION: self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION
        }

    @property
    def validators(self) -> dict:
        """RPC validators."""
        key = String(minLength=1, maxLength=256, nullable=False, title='cache key name')
        keys = Array(key, minItems=1)
        ttl = Integer(minimum=0, nullable=True, default=None, title='key lifetime in seconds')
        use_serializer = Boolean(default=True, title='use a default serializer for key values')
        return {
            **super().validators,
            'exists': Object(
                {
                    'key': key
                },
                required=['key'],
                title='check if cache key exists',
                additionalProperties=False
            ),
            'm_exists': Object(
                {
                    'keys': keys
                },
                required=['keys'],
                title='return existing keys from a given list',
                additionalProperties=False
            ),
            'get': Object(
                {
                    'key': key,
                    'use_serializer': use_serializer
                },
                required=['key'],
                title='get a key value',
                additionalProperties=False
            ),
            'm_get': Object(
                {
                    'keys': keys,
                    'use_serializer': use_serializer
                },
                required=['keys'],
                title='get multiple keys at once',
                additionalProperties=False
            ),
            'set': Object(
                {
                    'key': key,
                    'value': Generic(),
                    'use_serializer': use_serializer
                },
                required=['key', 'value'],
                title='set a key',
                additionalProperties=False
            ),
            'm_set': Object(
                {
                    'keys': Object(minProperties=1),
                    'ttl': ttl,
                    'use_serializer': use_serializer
                },
                required=['keys'],
                title='set multiple keys at once',
                additionalProperties=False
            ),
            'delete': Object(
                {
                    'key': key
                },
                required=['key'],
                title='remove a key',
                additionalProperties=False
            ),
            'm_delete': Object(
                {
                    'keys': keys
                },
                required=['keys'],
                title='remove multiple keys',
                additionalProperties=False
            )
        }

    async def init(self):
        """Service context init."""
        self._transport = self.discover_service(self._transport_name, cls=self.transport_cls)
        queue_settings = {
            'max_parallel_jobs': self.PARALLEL_JOBS,
            'max_queue_size': self.MAX_QUEUE_SIZE,
            'raise_exception': False
        }
        queue_settings.update(self._queue_settings)
        self._queue = ExecutorQueue(self.app, logger=self.logger, **queue_settings)
        await self._queue.init()

    @property
    def closed(self) -> bool:
        return self._queue is None

    async def close(self):
        """Service context close."""
        if not self.closed:
            await self._queue.close()
            self._queue = None

    async def exists(self, key: str, ignore_conn_errors=IGNORE_CONN_ERRORS) -> bool:
        """Check if key is present in the cache."""
        _key = self._create_key(key)
        result = await self._wrap_exec(self._exists(_key), ignore_conn_errors)
        if result is None:
            self.logger.info('Key "%s" -> "%s" not found.', key, _key)
        return bool(result)

    async def _exists(self, key: str) -> bool:
        """
        Should check if such key present and has not expired.
        Otherwise it should return False.
        """

    async def m_exists(self, keys: list, ignore_conn_errors=IGNORE_CONN_ERRORS) -> frozenset:
        """Returns a set of existing keys."""
        _keys = (self._create_key(key) for key in keys)
        self.logger.info('Looking for %d keys.', len(keys), extra={'keys': keys, '_keys': _keys})
        results = await self._wrap_exec(self._m_exists(*_keys), ignore_conn_errors)
        if results:
            return frozenset(key for key, result in zip(keys, results) if bool(result))
        else:
            return frozenset()

    @abc.abstractmethod
    async def _m_exists(self, *keys: str) -> list:
        """Should return a list of 0 and 1 (0 for not existing True for existing)."""

    async def get(self, key: str, use_serializer=True, ignore_conn_errors=IGNORE_CONN_ERRORS):
        """
        Get value of a key or None if not found.

        :param key: string only
        :param use_serializer: to use serializer for value decoding (False = return raw)
        :param ignore_conn_errors: set True to ignore connection errors and skip the operation
        """
        _key = self._create_key(key)
        self.logger.info('Looking for key "%s" -> "%s".', key, _key)
        value = await self._wrap_exec(self._get(_key), ignore_conn_errors)
        value = self._load_value(value, use_serializer)
        if value is None:
            self.logger.info('Key "%s" -> "%s" not found.', key, _key)
        return value

    @abc.abstractmethod
    async def _get(self, key: str) -> Optional:
        """Should return a key value or None if not found."""

    async def m_get(self, keys: list, use_serializer=True, ignore_conn_errors=IGNORE_CONN_ERRORS) -> dict:
        """
        Get values of multiple keys.

        :param keys: list of keys
        :param use_serializer: use a serializer for value decoding (False = return raw)
        :param ignore_conn_errors: set True to ignore connection errors and skip the operation
        """
        _keys = [self._create_key(key) for key in keys]
        self.logger.info('Looking for %d keys.', len(keys), extra={'keys': keys, '_keys': _keys})
        values = await self._wrap_exec(self._m_get(*_keys), ignore_conn_errors)
        if values:
            result = {
                k: self._load_value(v, use_serializer)
                for k, v in zip(keys, values) if v
            }
        else:
            result = {}
        return result

    @abc.abstractmethod
    async def _m_get(self, *keys: str) -> list:
        """Should return a list of values for given keys (None for expired or not present values)."""

    async def set(
            self, key: str, value, ttl: int = None, use_serializer=True,
            ignore_conn_errors=IGNORE_CONN_ERRORS, nowait=NOWAIT):
        """
        Set a single key.

        :param key: string only
        :param value: any serializable value
        :param ttl: key lifetime in seconds, 0 for infinite, None for default
        :param use_serializer: use a serializer for value encoding (False = return raw)
        :param ignore_conn_errors: set True to ignore connection errors and skip the operation
        :param nowait: set operation in background (don't wait for response)
        """
        if ttl is None:
            _ttl = self._default_ttl
        else:
            _ttl = ttl
        _key = self._create_key(key)
        self.logger.info('Setting key "%s" -> "%s".', key, _key)
        value = self._dump_value(value, use_serializer)
        if nowait:
            await self._queue.put(self._set, (_key, value, _ttl))
        else:
            await self._wrap_exec(self._set(_key, value, _ttl), ignore_conn_errors)

    @abc.abstractmethod
    async def _set(self, key: str, value, ttl: int):
        """Set a key value with ttl in sec (0 for infinite)."""

    async def m_set(
            self, keys: dict, ttl: int = None, use_serializer=True,
            ignore_conn_errors=IGNORE_CONN_ERRORS, nowait=NOWAIT):
        """
        Set multiple keys.

        :param keys: <key>: <value>
        :param ttl: lifetime in seconds, 0 for infinite, None for default
        :param use_serializer: use a serializer for value encoding (False = return raw)
        :param ignore_conn_errors: set True to ignore connection errors and skip the operation
        :param nowait: set operation in background (don't wait for response)
        """
        if ttl is None:
            _ttl = self._default_ttl
        else:
            _ttl = ttl
        key_dict = {
            self._create_key(k): self._dump_value(v, use_serializer)
            for k, v in keys.items()
        }
        _keys = list(keys.keys())
        self.logger.info('Setting %d keys.', len(keys), extra={'keys': keys.keys(), '_keys': _keys})
        if nowait:
            await self._queue.put(self._m_set, (key_dict, _ttl))
        else:
            await self._wrap_exec(self._m_set(key_dict, _ttl), ignore_conn_errors)

    @abc.abstractmethod
    async def _m_set(self, keys: dict, ttl: int):
        """Set multiple keys at once with ttl in sec (0 for inf)."""

    async def delete(self, key: str, ignore_conn_errors=IGNORE_CONN_ERRORS, nowait=NOWAIT):
        """Removes a key from cache."""
        _key = self._create_key(key)
        self.logger.info('Removing key "%s" -> "%s".', key, _key)
        if nowait:
            await self._queue.put(self._delete, (_key,))
        else:
            await self._wrap_exec(self._delete(_key), ignore_conn_errors)

    @abc.abstractmethod
    async def _delete(self, key: str):
        """Remove one key at once."""

    async def m_delete(self, keys: list, ignore_conn_errors=IGNORE_CONN_ERRORS, nowait=NOWAIT):
        """Remove multiple keys at once."""
        _keys = [self._create_key(key) for key in keys]
        self.logger.info('Removing %d keys.', len(keys), extra={'keys': keys, '_keys': _keys})
        if nowait:
            await self._queue.put(self._m_delete, tuple(_keys))
        else:
            await self._wrap_exec(self._m_delete(*_keys), ignore_conn_errors)

    @abc.abstractmethod
    async def _m_delete(self, *keys: str):
        """Remove multiple keys at once."""

    async def _wrap_exec(self, f, ignore_conn_errors: bool):
        try:
            return await f
        except self.CONNECTION_ERROR_CLASSES:
            if not ignore_conn_errors:
                raise

    def _create_key(self, key: str):
        keys = (self.app.env, self._namespace, self.PREFIX, key)
        return self.DELIMITER.join((k for k in keys if k))

    def _load_value(self, value, use_serializer: bool):
        if value is None:
            return
        elif use_serializer:
            return self._serializer.loads(value)
        else:
            return value

    def _dump_value(self, value, use_serializer: bool):
        if use_serializer:
            return self._serializer.dumps(value)
        else:
            return value
