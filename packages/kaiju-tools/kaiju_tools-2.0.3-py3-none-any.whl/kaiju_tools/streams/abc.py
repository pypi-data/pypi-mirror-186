import abc
import asyncio
import uuid
from typing import Awaitable, List, Optional, Union

from kaiju_tools.encoding import serializers, MimeTypes, SerializerInterface
from kaiju_tools.exceptions import ensure_traceback
from kaiju_tools.services import ContextableService, Service
from kaiju_tools.rpc import JSONRPCServer, ServerSessionFlag, AbstractRPCCompatible
from kaiju_tools.rpc.etc import JSONRPCHeaders
from kaiju_tools.rpc.jsonrpc import RPCRequest, RPCResponse, RPCError
from kaiju_tools.locks import BaseLocksService, LockAcquireTimeout

from .etc import Headers, Topics

__all__ = ['Consumer', 'Producer', 'Listener', 'CallbackService']


class CallbackService(abc.ABC):

    @abc.abstractmethod
    async def rpc_callback(self, headers: dict, body: RPCResponse):
        ...

    @abc.abstractmethod
    async def rpc_callback_error(self, headers: dict, error: RPCError):
        ...


class Consumer(ContextableService, abc.ABC):
    """
    Base consumer class.
    """

    content_type = MimeTypes.msgpack
    PREFIX = 'stream'
    DELIMITER = '-'

    def __init__(
        self, app, topic: str, rpc_service: JSONRPCServer,
        transport: Service, locks_service: BaseLocksService, callback_service: CallbackService = None,
        namespace: str = None, serializers=serializers, content_type=content_type, logger=None,
        producer: 'Producer' = None, **settings
    ):
        """
        :param app:
        :param topic:
        :param settings: additional consumer settings
        :param namespace: None == app.name
        :param serializers:
        :param content_type:
        :param transport_service: transport service name
        :param locks_service: locks service name
        :param callback_service: you may provide a callback service for processing responses
        :param producer: a producer instance for executing callbacks (if requested)
        :param logger:
        """
        self.topic_name = topic
        self.namespace = namespace if namespace else app.name
        self.topic = self.get_topic_key(app.env, self.namespace, self.topic_name)
        super().__init__(app=app, logger=logger)
        self._settings = settings
        self._rpc = rpc_service
        self.locking_key = self.get_locking_key(self.namespace, self.topic_name)
        self._serializer: SerializerInterface = serializers[content_type]
        self._transport = transport
        self._locks: BaseLocksService = locks_service
        self._producer = producer
        self._callback_service = callback_service
        self._closing = True
        self._task = None
        self._consumer = None
        self._ready = asyncio.Event()
        self._unlocked = asyncio.Event()

    async def init(self):
        self._closing = False
        await self._locks.wait(self.locking_key, timeout=None)
        self._unlocked.set()
        self._task = asyncio.create_task(self._loop())
        await self._ready.wait()

    @property
    def closed(self) -> bool:
        return self._task is None

    async def close(self):
        if not self.closed:
            self._closing = True
            if self._ready.is_set():
                self._task.cancel()
            else:
                await self._task
            self._task = None

    @property
    def locked(self):
        return not self._unlocked.is_set()

    async def check_topic_lock(self):
        """Checks a topic lock and stops if one is present."""
        try:
            await self._locks.wait(key=self.locking_key, timeout=0.000001)
        except LockAcquireTimeout:
            # means that the lock exists
            self._unlocked.clear()
            await self._ready.wait()

    async def lock(self):
        """Lock the topic (will not consume new messages)."""
        self.logger.debug('Locking...')
        self._unlocked.clear()
        await self._locks.acquire(self.locking_key, identifier=self.topic)
        await self._ready.wait()
        self.logger.debug('Locked.')

    async def unlock(self):
        """Unlock the topic (will start consuming messages)."""
        self._unlocked.set()
        await self._locks.release(self.locking_key, identifier=self.topic)
        self.logger.info('Unlocked.')

    @classmethod
    def get_topic_key(cls, env: str, namespace: str, topic: str) -> str:
        s = (env, namespace, cls.PREFIX, topic)
        return cls.DELIMITER.join(s)

    @classmethod
    def get_locking_key(cls, namespace: str, topic: str) -> str:
        s = (namespace, cls.PREFIX, topic)  # env is auto-added by a locks service
        return cls.DELIMITER.join(s)

    @abc.abstractmethod
    async def _init(self):
        """Define your consumer start here."""

    @abc.abstractmethod
    async def _close(self):
        """Define your consumer stop here."""

    @abc.abstractmethod
    async def _get_message_batch(self):
        """
        You should define your own backend specific method of receiving a batch of messages.
        It should return a new offset position
        """

    @abc.abstractmethod
    async def _process_batch(self, batch):
        """
        Define your own message processing and commit here.
        """

    async def _loop(self):
        _logger = self.logger
        _logger.debug('Starting.')
        await self._init()

        await self.app.services.initialized.wait()

        _logger.debug('Started.')

        while not self._closing:
            self._ready.set()
            await self._unlocked.wait()
            try:
                batch = await self._get_message_batch()
                self._ready.clear()
                await self._process_batch(batch)
            except Exception as exc:
                _logger.error(
                    'There was an exception in the consumer loop: %s',
                    exc, exc_info=(type(exc), exc, exc.__traceback__))

        self.logger.debug('Closing.')
        await self._close()
        self.logger.debug('Closed.')

    def _create_response_object(self, body):
        if isinstance(body, (list, tuple)):
            return [self._create_response_object(item) for item in body]
        else:
            if 'error' in body:
                return RPCError(**body)
            else:
                return RPCResponse(**body)

    async def _process_request(self, headers, body):
        """Process an RPC request or a request batch."""
        if not body:
            return
        try:
            value = self._serializer.loads(body)
            e = None

            # response processing

            if headers and Headers.callback_response in headers:
                callback = headers[Headers.callback_response]
                if callback == self.topic:
                    if self._callback_service:
                        value = self._create_response_object(value)
                        await self._call_callback_service(headers, value)
                    else:
                        self.logger.info(
                            'Unconsumed callback (callback service is not available).',
                            extra={'topic': self.topic})
                else:
                    self.logger.info(
                        'Unconsumed callback (due to non-matching topic).',
                        extra={'callback': callback, 'topic': self.topic})
                return

            # request processing

            if isinstance(value, (list, dict, tuple)):
                self.logger.info('<- %s', value)
                response_headers, result = await self._rpc.call(value, headers=headers, session=ServerSessionFlag)
                if isinstance(result, RPCError):
                    e = result
                elif isinstance(result, (list, tuple)):
                    e = next((r for r in result if isinstance(r, RPCError)), None)
                self.logger.info('-> %s', result)
                if self._producer:
                    callback = self._get_callback_topic(headers)
                    if callback:
                        if response_headers is None:
                            response_headers = {}
                        response_headers[Headers.callback_response] = callback
                        await self._callback(callback, response_headers, result)
            else:
                self.logger.error(
                    'Unsupported RPC request body.',
                    extra={'headers': headers, 'body': body})

            if e:
                ensure_traceback(e)
                self.logger.error(
                    '%s', e.repr(), extra={'error': e.repr()},
                    exc_info=(type(e), e, e.__traceback__))
                raise e

        except Exception as exc:
            self.logger.error(
                'Error processing a message. %s', exc,
                exc_info=(type(exc), exc, exc.__traceback__),
                extra={'headers': headers, 'body': body})

    @staticmethod
    def _get_callback_topic(headers) -> Optional[str]:
        if headers:
            callback = headers.get(Headers.callback)
            if type(callback) is bytes:
                callback = callback.decode('utf-8')
            return callback

    async def _call_callback_service(self, headers, body):
        if isinstance(body, RPCError):
            await self._callback_service.rpc_callback_error(headers, body)
        elif isinstance(body, RPCResponse):
            await self._callback_service.rpc_callback(headers, body)
        elif isinstance(body, list):
            await asyncio.gather(*(
                self._call_callback_service(headers, res)
                for res in body
            ))
        else:
            self.logger.error('Unexpected callback body type: %s.', type(body))

    def _callback(self, topic: str, headers: dict, result: Union[RPCResponse, RPCError]) -> Awaitable:
        data = self._serializer.dumps_bytes(result)
        return self._producer._send_request(topic=topic, key=None, request=data, headers=headers)

    def _get_logger_name(self):
        return f'{self.__class__.__name__}.{self.topic}'


class Producer(ContextableService, abc.ABC):
    """
    A base producer class.
    """

    content_type = MimeTypes.msgpack

    def __init__(
        self, app, transport: Service, namespace: str = None,
        serializers=serializers, content_type=content_type, logger=None,
        **settings
    ):
        """
        :param app:
        :param transport: transport service name
        :param namespace: app name or namespace
        :param env: environment name
        :param settings: additional producer settings
        :param serializers:
        :param content_type: MIME type
        :param logger:
        """
        super().__init__(app=app, logger=logger)
        self._env = app.env
        self._namespace = namespace if namespace else app.name
        self._transport = transport
        self._settings = settings
        self._serializer: SerializerInterface = serializers[content_type]
        self._closing = False
        self._closed = False

    async def init(self):
        self._closing = False
        await self._init()
        self._closed = False

    async def close(self):
        self._closing = True
        await self._close()
        self._closed = True

    @property
    def closed(self):
        return self._closed

    async def init_topic(self, topic: str):
        topic = Consumer.get_topic_key(self._env, self._namespace, topic)
        self.logger.info('Starting topic "%s".', topic, extra={'topic': topic})
        result = await self._send_request(topic, None, None, b'')
        self.logger.debug(result)

    def send(self, namespace: str, topic: str, body, key: str = None, headers: dict = None, **kws) -> Awaitable:
        """Send arbitrary data to a specific topic."""
        if self._closing:
            raise RuntimeError('The producer is closing.')
        topic = Consumer.get_topic_key(self._env, namespace, topic)
        self.logger.info('-> [%s] %s', topic, body, extra={'topic': topic, 'headers': headers, 'body': body})
        data = self._serializer.dumps_bytes(body)
        return self._send_request(topic, key, headers, data, **kws)

    def call(
        self, method: str, params: dict = None, namespace: str = None, topic: str = None,
        key: str = None, headers: dict = None, callback: str = None, **kws
    ) -> Awaitable:
        """
        Make an RPC call to a topic.

        :param namespace: app or namespace name (None for current)
        :param topic: topic name (None for default)
        :param method: RPC method name
        :param params: RPC method arguments
        :param key: optional unique message key (can be used by kafka or other queues for 'compaction')
        :param headers: optional message headers (will be also delivered to an RPC server)
        :param callback: optional callback topic
        """
        if self._closing:
            raise RuntimeError('The producer is closing.')
        if namespace is None:
            namespace = self._namespace
        if topic is None:
            topic = Topics.rpc
        topic = Consumer.get_topic_key(self._env, namespace, topic)
        headers = self._create_headers(headers, callback)
        default_id = False if callback else None  # generate id only if needed
        data = self._serializer.dumps_bytes(RPCRequest(default_id, method, params))
        return self._send_request(topic, key, headers, data, **kws)

    def call_multiple(
        self, data: list, namespace: str = None, topic: str = None,
        key: str = None, headers: dict = None, callback: str = None, **kws
    ):
        """
        Make a batch RPC call to a topic.

        :param namespace: app or namespace name (None for current)
        :param topic: topic name (None for default)
        :param data: an rpc request batch (each with 'method' and 'params' and optional 'id')
        :param key: optional unique message key (can be used by kafka or other queues for 'compaction')
        :param headers: optional message headers (will be also delivered to an RPC server)
        :param callback: optional callback topic
        """
        if self._closing:
            raise RuntimeError('The producer is closing.')
        if namespace is None:
            namespace = self._namespace
        if topic is None:
            topic = Topics.rpc
        topic = Consumer.get_topic_key(self._env, namespace, topic)
        headers = self._create_headers(headers, callback)
        default_id = False if callback else None  # generate id only if needed
        batch = [
            RPCRequest(row.get('id', default_id), row['method'], row.get('params'))
            for row in data
        ]
        data = self._serializer.dumps_bytes(batch)
        return self._send_request(topic, key, headers, data, **kws)

    @abc.abstractmethod
    async def _init(self):
        """Define your producer init code here."""

    @abc.abstractmethod
    async def _close(self):
        """Define your producer close code here."""

    @abc.abstractmethod
    async def _send_request(self, topic: str, key: Optional, headers: Optional[dict], request: bytes, **kws):
        """Define your send request code here."""

    def _create_headers(self, headers, callback) -> dict:
        if headers is None:
            headers = {}
        if callback:
            callback = Consumer.get_topic_key(self._env, self._namespace, callback)
            headers[Headers.callback] = callback
        if JSONRPCHeaders.CORRELATION_ID_HEADER not in headers:
            headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = str(uuid.uuid4())
        headers[JSONRPCHeaders.APP_ID_HEADER] = str(self.app.id)
        return headers


class Listener(ContextableService, AbstractRPCCompatible):
    """
    Base listener class combining multiple consumers, producers, lock / unlock interface and a web interface.
    """

    service_name = 'streams'
    content_type = MimeTypes.msgpack
    refresh_rate = 1.0
    consumer_class = Consumer  #: you have to specify it in your implementation
    producer_class = Producer  #: you have to specify it in your implementation
    transport_class = None  #: you should specify your transport class here
    locks_service_class = BaseLocksService
    rpc_service_class = JSONRPCServer

    def __init__(
        self, app, namespace: str = None, topics: List[str] = None, transport: str = None, locks_service: str = None,
        callbacks: list = None, rpc_service: str = None, consumer_settings: dict = None, producer_settings: dict = None,
        serializers=serializers, content_type=content_type, refresh_rate: float = refresh_rate,
        permissions=None, logger=None
    ):
        ContextableService.__init__(self, app=app, logger=logger)
        AbstractRPCCompatible.__init__(self, permissions=permissions)
        self.topics = list(topics) if topics else []
        self.namespace = namespace if namespace else app.name
        self._env = self.app.env
        self._rpc_service_name = rpc_service
        self._transport_name = transport
        self._locks_service_name = locks_service
        self._consumer_settings = consumer_settings if consumer_settings else {}
        self._producer_settings = producer_settings if producer_settings else {}
        self._serializers = serializers
        self.content_type = content_type
        self.refresh_rate = max(1., float(refresh_rate))
        self._callbacks_settings = callbacks if callbacks else []
        self._callbacks = {}
        self._rpc = None
        self._transport = None
        self._locks = None
        self._producer = None
        self._task = None
        self._consumers = {}
        self._closing = True

    @property
    def routes(self) -> dict:
        return {
            'status': self.get_status,
            'lock_all': self.lock_all,
            'unlock_all': self.unlock_all,
            'lock_topic': self.lock_topic,
            'unlock_topic': self.unlock_topic,
            'call': self.call,
            'call_multiple': self.call_multiple
        }

    @property
    def permissions(self) -> dict:
        return {
            '*': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION
        }

    async def init(self):
        self._closing = False
        self._rpc = self.discover_service(self._rpc_service_name, cls=self.rpc_service_class)
        if self.transport_class is None and not self._transport_name:
            self._transport = None
        else:
            self._transport = self.discover_service(self._transport_name, cls=self.transport_class)
        self._locks = self.discover_service(self._locks_service_name, cls=self.locks_service_class)

        if self._callbacks_settings:
            for callback in self._callbacks_settings:
                topic, service = callback['topic'], callback['service']
                service = self.discover_service(service, cls=CallbackService)
                self._callbacks[topic] = service

        self._producer = self.producer_class(
            app=self.app,
            namespace=self.namespace,
            transport=self._transport,
            serializers=self._serializers,
            content_type=self.content_type,
            logger=self.logger,
            **self._producer_settings)
        await self._producer.init()
        for topic in self.topics:
            await self._producer.init_topic(topic)

        await self._init()
        self._task = asyncio.create_task(self._loop())

    def closed(self):
        return self._consumers is None

    async def close(self):
        if not self.closed:
            self._closing = True
            if self._task:
                await self._task
                self._task = None
            try:
                await self._close_consumers()
                self._consumers = {}
            finally:
                await self._producer.close()

    def add_topic(self, topic: str):
        if not self.closed:
            raise RuntimeError('Adding a new topic is only allowed when the listener is closed.')
        if topic not in self.topics:
            self.topics.append(topic)

    async def call(
        self, method: str, params: dict = None, namespace: str = None, topic: str = None,
        key: str = None, headers: dict = None, callback: str = None, **kws
    ) -> Awaitable:
        """
        Make an RPC call to a topic.

        :param namespace: app or namespace name (None for current)
        :param topic: topic name (None for default)
        :param method: RPC method name
        :param params: RPC method arguments
        :param key: optional unique message key (can be used by kafka or other queues for 'compaction')
        :param headers: optional message headers (will be also delivered to an RPC server)
        :param callback: optional callback topic
        """
        return await self._producer.call(
            method=method, params=params, namespace=namespace, topic=topic, key=key,
            headers=headers, callback=callback, **kws)

    async def call_multiple(
        self, data: list, namespace: str = None, topic: str = None,
        key: str = None, headers: dict = None, callback: str = None, **kws
    ):
        """
        Make a batch RPC call to a topic.

        :param namespace: app or namespace name (None for current)
        :param topic: topic name (None for default)
        :param data: an rpc request batch (each with 'method' and 'params' and optional 'id')
        :param key: optional unique message key (can be used by kafka or other queues for 'compaction')
        :param headers: optional message headers (will be also delivered to an RPC server)
        :param callback: optional callback topic
        """
        return await self._producer.call_multiple(
            data=data, namespace=namespace, topic=topic, key=key, headers=headers, callback=callback,
            **kws)

    async def get_status(self) -> dict:
        """Returns a list of topics and current consumer status."""
        return {
            'topics': list(self._consumers.keys()),
            'consumers': [
                {
                    'topic': consumer.topic_name,
                    'topic_fullname': consumer.topic,
                    'locking_key': consumer.locking_key,
                    'locked': consumer.locked,
                    'closed': consumer.closed
                }
                for consumer in self._consumers.values()
            ],
            'consumer_settings': self._consumer_settings,
            'producer_settings': self._producer_settings
        }

    async def lock_topic(self, topic: str):
        """Lock a topic and stop all topic consumers."""
        if topic in self._consumers:
            consumer = self._consumers[topic]
            await consumer.lock()
            await asyncio.sleep(self.refresh_rate)

    async def unlock_topic(self, topic):
        """Unlock a topic and resume topic consumers."""
        if not self._closing and topic in self._consumers:
            consumer = self._consumers[topic]
            await consumer.unlock()

    async def lock_all(self):
        """Lock all topics."""
        await asyncio.gather(*(
            self.lock_topic(topic)
            for topic in self._consumers.keys()
        ))

    async def unlock_all(self):
        """Unlock all topics."""
        await asyncio.gather(*(
            self.unlock_topic(topic)
            for topic in self._consumers.keys()
        ))

    async def _loop(self):
        self.logger.info('Starting the watcher loop.')
        while not self._closing:
            try:
                await self._init_consumers()
                await self._check_locks()
                await self._daemon_task()
                await asyncio.sleep(self.refresh_rate)
            except Exception as exc:
                self.logger.error(
                    'There was an exception in the loop. %s',
                    exc, exc_info=(type(exc), exc, exc.__traceback__))

    async def _init(self):
        """Custom init hook for a listener class."""

    async def _daemon_task(self):
        """You may define your loop daemon task here."""

    async def _init_consumers(self):
        """Initializes all consumers which don't exist."""
        _start = []
        for topic in self.topics:
            if topic not in self._consumers:
                _start.append(self._start_consumer(topic))
        await asyncio.gather(*_start)

    async def _close_consumers(self):
        await asyncio.gather(*(
            self._close_consumer(topic)
            for topic in self._consumers.keys()
        ))

    async def _start_consumer(self, topic: str):
        if not self._closing and topic not in self._consumers:
            callback = self._callbacks.get(topic)
            self.logger.debug(
                'Starting a new consumer for topic "%s" with callback "%s".',
                topic, callback)
            consumer: Consumer = self.consumer_class(
                app=self.app,
                namespace=self.namespace,
                topic=topic,
                transport=self._transport,
                locks_service=self._locks,
                callback_service=callback,
                rpc_service=self._rpc,
                producer=self._producer,
                serializers=self._serializers,
                content_type=self.content_type,
                logger=self.logger,
                **self._consumer_settings)
            await consumer.init()
            self._consumers[topic] = consumer

    async def _close_consumer(self, topic: str):
        if topic in self._consumers:
            consumer = self._consumers[topic]
            await consumer.close()

    async def _check_locks(self):
        await asyncio.gather(*(
            consumer.check_topic_lock()
            for consumer in self._consumers.values()
        ))
