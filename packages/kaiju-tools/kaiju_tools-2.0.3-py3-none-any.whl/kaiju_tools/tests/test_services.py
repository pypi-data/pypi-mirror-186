import pytest

from ..services import *


@pytest.mark.asyncio
async def test_service_context_manager_basic_functions(aiohttp_server, application, logger):

    class SomeSuperService(ServiceOfServices):

        def __init__(self, *args, **kws):
            super().__init__(*args, **kws)
            self.services = {}

        def register_service(self, service_name: str, service: Service):
            self.services[service_name] = service

    class SimpleUnnamedService(Service):

        def __init__(self, x, *args, **kws):
            super().__init__(*args, **kws)
            self.x = x

        def __call__(self, *args, **kwargs):
            return self.x

    class SimpleUnnamedServiceWithDefaults(Service):

        def __init__(self, x, *args, **kws):
            super().__init__(*args, **kws)
            self.x = x

        def __call__(self, *args, **kwargs):
            return self.x

    class _ContextableService(ContextableService):

        service_name = 'contextable_service'

        def __init__(self, x, *args, **kws):
            super().__init__(*args, **kws)
            self.x = x
            self.y = None

        def closed(self) -> bool:
            return self.y is None

        async def init(self):
            self.y = self.x

        async def close(self):
            self.y = None

        def call(self, *args, **kwargs):
            return self.y

    class ContextableFailedService(_ContextableService):

        service_name = 'contextable_failed'

        def __init__(self, *args, **kws):
            super().__init__(*args, **kws)
            self.y = 42

        async def init(self):
            raise ValueError()

    class ContextableDoubleFailedService(ContextableFailedService):

        service_name = 'contextable_double_failed'

        async def close(self):
            raise ValueError()

    settings = [
        {
            'cls': 'SomeSuperService'
        },
        {
            'cls': 'SimpleUnnamedService',
            'register_in_app': True,
            'settings': {
                'x': 42
            }
        },
        {
            'cls': 'SimpleUnnamedServiceWithDefaults',
            'register_in_services': ['SomeSuperService'],
            'settings': {
                'x': 42
            }
        },
        {
            'cls': 'SimpleUnnamedService',
            'name': 'another_simple_unnamed',
            'register_in_app': True,
            'register_in_services': 'SomeSuperService',
            'settings': {
                'x': 43
            }
        },
        {
            'cls': '_ContextableService',
            'settings': {
                'x': 44
            }
        },
        {
            'cls': 'ContextableFailedService',
            'required': False,
            'settings': {
                'x': 44
            }
        },
        {
            'cls': 'ContextableDoubleFailedService',
            'required': False,
            'settings': {
                'x': 44
            }
        },
        {
            'cls': 'SimpleUnnamedService',
            'name': 'unregistered',
            'register_in_app': False,
            'settings': {
                'x': 42
            }
        }
    ]

    application = application()
    registry = ServiceClassRegistry()
    registry.register_classes_from_namespace(locals())

    manager = ServiceContextManager(
        application, class_registry=registry, settings=settings,
        logger=logger)

    # checking that all needed services were registered in a super service

    assert 'SimpleUnnamedServiceWithDefaults' in manager.SomeSuperService.services
    assert 'another_simple_unnamed' in manager.SomeSuperService.services
    assert 'SimpleUnnamedService' not in manager.SomeSuperService.services

    # testing app initialization

    application.cleanup_ctx.extend(manager)
    await aiohttp_server(application)

    # checking that all needed services were registered
    assert application.SimpleUnnamedService is application.services.SimpleUnnamedService
    assert application['SimpleUnnamedService'] is application.services.SimpleUnnamedService

    # checking all services are OK
    assert application.services.SimpleUnnamedService() == 42
    assert application.services.another_simple_unnamed() == 43
    assert application.services.contextable_service.call() == 44
    assert 'unregistered' not in application

