import asyncio
import uuid

from kaiju_tools.rpc import AbstractRPCCompatible, JSONRPCServer
from kaiju_tools.services import Service

from ..abc import Listener, CallbackService
from ..etc import Topics


class TestCallback(Service, CallbackService):
    service_name = 'pytest.callback'

    def __init__(self, app, logger):
        Service.__init__(self, app=app, logger=logger)
        self.callbacks = []
        self.errors = []

    async def rpc_callback(self, headers, body):
        self.logger.info('Callback received: %s.', body)
        self.callbacks.append(body)

    async def rpc_callback_error(self, headers, error):
        self.logger.info('Callback error received: %s.', error)
        self.errors.append(error)


class TestService(Service, AbstractRPCCompatible):
    service_name = 'pytest'

    def __init__(self, app, logger):
        Service.__init__(self, app, logger=logger)
        self.data = {}
        self.error = None

    @property
    def routes(self):
        return {
            'get': self.get,
            'write': self.write,
            'delete': self.delete
        }

    async def get(self, key: str):
        try:
            self.logger.info('Getting "%s" from "%s".', key, self.data)
            value = self.data.get(key)
        except Exception as exc:
            self.error = exc
            raise
        else:
            return value

    async def write(self, key: str, value):
        try:
            self.logger.info('Writing "%s":"%s" to "%s".', key, value, self.data)
            self.data[key] = value
        except Exception as exc:
            self.error = exc
            raise
        else:
            return value

    async def delete(self, key: str):
        try:
            self.logger.info('Removing "%s" from "%s".', key, self.data)
            del self.data[key]
        except Exception as exc:
            self.error = exc
            raise
        else:
            return


async def stream_test_function(listener, logger):

    async def _wait(cond):
        await asyncio.sleep(0.1)
        dt = 0
        while not cond and dt < 10:
            dt += 0.1
            await asyncio.sleep(0.1)

    logger.info('Testing init.')
    listener: Listener = listener
    ns = listener.app.name
    rpc: JSONRPCServer = listener._rpc_service_name
    service = TestService(listener.app, logger)
    callback = TestCallback(listener.app, logger)
    rpc.register_service(service.service_name, service)
    locks = listener._locks_service_name
    topic = Topics.rpc
    callback_topic = Topics.callback
    listener._callbacks_settings = [
        {
            'topic': callback_topic,
            'service': callback
        }
    ]
    async with rpc:
        async with locks:
            async with listener:
                logger.info("Testing basic operation.")

                logger.info("Testing basic calls.")

                key, value = 'key', uuid.uuid4()
                await listener.call(ns, topic, 'pytest.write', {'key': key, 'value': value}, wait=True)
                await _wait(service.data)
                assert service.data[key] == value

                logger.info("Testing error handling and multi-calls.")

                await listener.call_multiple(
                    ns, topic, [
                        {'method': 'pytest.delete', 'params': {'key': 'not-key'}},
                        {'method': 'pytest.delete', 'params': {'key': key}}
                    ]
                )
                await _wait(service.error)
                assert type(service.error) is KeyError, 'should raise a key error'
                assert key not in service.data, 'valid operations should proceed'
                service.error = None

                logger.info('Testing topic locking.')

                await listener.lock_topic(topic)
                await listener.call(ns, topic, 'pytest.write', {'key': key, 'value': value})
                await asyncio.sleep(0.1)
                assert key not in service.data, 'should not yet have a value'

                logger.info('Testing topic status.')

                status = await listener.get_status()
                status = next((s for s in status['consumers'] if s['topic'] == topic))
                assert status['locked'] is True

                logger.info('Testing topic unlocking.')

                await listener.unlock_topic(topic)
                await _wait(service.data)
                assert key in service.data
                service.data = {}

                logger.info('Testing all-topic locking / unlocking (should perform in the same way).')

                await listener.lock_all()
                await listener.call(ns, topic, 'pytest.write', {'key': key, 'value': value})
                await asyncio.sleep(0.1)
                assert key not in service.data, 'should not yet have a value'
                await listener.unlock_all()
                await _wait(service.data)
                assert key in service.data
                status = await listener.get_status()
                status = next((s for s in status['consumers'] if s['topic'] == callback_topic))
                assert status['locked'] is False

                logger.info('Testing callbacks.')

                service.data = {}
                await listener.call(ns, callback_topic, 'pytest.write', {'key': key, 'value': value})
                await _wait(service.data)
                assert key in service.data, 'callback consumer should be available'

                await listener.call(ns, topic, 'pytest.get', {'key': key}, callback=callback_topic)
                await _wait(callback.callbacks)
                assert callback.callbacks[0].result == value
