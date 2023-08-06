"""
Service and service manager classes.

Service
-------

Basically any class what performs a bunch of logically connected operations
in an app should be a :class:`.Service` (which also provides logging).

.. code-block:: python

    from kaiju_tools.services import Service

    class MyService(Service):
        pass


If a service needs to be initialized asynchronously, it should be a subclass
of :class:`.ContextableService`, where you will need to implement `closed` property
and may need to insert your custom logic into `init` and `close` methods.

.. code-block:: python

    from kaiju_tools.services import ContextableService

    class MyService(ContextableService):
        # this service can be initialized asynchronously by a context manager

        async def init(self):
            await self.do_something_async()
            self._closed = False

        async def close(self):
            await self.undo_something_async()
            self._closed = True

        @property
        def closed(self):
            return self._closed


If a service can hold other services, you may make it a subclass of :class:`.ServiceOfServices`
and implement `register_service` method. After that the context manager can automatically
register other services which have `register_in` setting parameter set to the
service name

.. code-block:: python

    from kaiju_tools.services import ServiceOfServices

    class MyService(ServiceOfServices):

        def register_service(self, service_name, service):
            self._services.append(service)


Service context manager
-----------------------

Service context manager handles multiple services initialization and de-initialization.

Service initialization diagram (I)
----------------------------------

This stage is called on `__init__()` of a :class:`.ServiceContextManager`
instance. At this stage class configurations will be parsed and all service instances
will be created and registered in the context manager.

.. image:: ../images/ServiceContextManagerAD_1.png

Service initialization diagram (II)
-----------------------------------

This stage is called when the app async context is being initialized. It creates
cleanup contexts for all :class:`.ContextableService` services and registers
them in the app's cleanup context, thus services `init()` and `close()` procedures
can be performed on startup and on cleanup application phases.

.. image:: ../images/ServiceContextManagerAD_2.png

Classes
-------

"""

import abc
import asyncio
import logging
from collections import OrderedDict
from functools import partial
from typing import Union, Iterable, List, Type, Dict, Optional

from aiohttp.web import Application

from .class_registry import AbstractClassRegistry
from .logging import Loggable
from .serialization import Serializable
from .exceptions import InvalidLicense

__all__ = [
    'App', 'Service', 'Contextable', 'Loggable', 'ContextableService', 'ServiceOfServices',
    'ServiceClassRegistry', 'service_class_registry',
    'ServiceSettings', 'ServiceConfigurationError', 'ServiceContextManager'
]


class App(Application):
    """Web application interface."""

    id: str
    name: str
    version: str
    env: str
    debug: bool
    loglevel: str
    logger: logging.Logger
    services: 'ServiceContextManager'
    settings: dict


class Service(Loggable, abc.ABC):
    """
    A simple web application service.

    :param app: aiohttp web application
    :param logger: a logger instance (None for default)
    """

    service_name = None   #: you may define a custom service name here

    def __init__(self, app: App = None, logger=None):
        Loggable.__init__(self, logger=self._get_parent_logger(app, logger))
        self.app = app

    @staticmethod
    def _get_parent_logger(app, logger):
        if app is not None and logger is None:
            return app.logger
        else:
            return logger

    def discover_service(
        self, name: Union[str, 'Service', None],
        cls: Union[Union[str, Type], Iterable[Union[str, Type]]] = None,
        required=True
    ):
        """
        This method will try to discover a service using specified name and/or service
        class.

        :param name: specify a service name or service instance (in latter case
            it will be returned as is)
            False means that nothing will be returned, i.e. service will be disabled
        :param cls: specify service class. If name wasn't specified, then the first
            service matching given class will be returned. If name and class
            both were specified, then the type check will be performed on a newly
            discovered service
        :param required: means that an exception will rise if service doesn't exist
            otherwise in this case None will be returned
        """

        if name is False and not required:
            return
        elif isinstance(name, Service):
            return name
        else:
            return self.app.services.discover_service(name=name, cls=cls, required=required)


class ServiceOfServices(Service, abc.ABC):
    """Service which also can hold another services."""

    @abc.abstractmethod
    def register_service(self, service_name: str, service: Service):
        """Here you can create whatever code you want to register another
        service in it. The context manager will automatically try to perform
        the task if it will receive an appropriate instruction for it."""


class Contextable(abc.ABC):

    async def init(self):
        """Define your asynchronous initialization here."""

    async def close(self):
        """Define your asynchronous de-initialization here."""

    @property
    def closed(self) -> bool:
        """Must return True if `close()` procedure has been successfully executed."""

        return False

    async def __aenter__(self):
        await self.init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class ContextableService(Service, Contextable):
    """A service which must be asynchronously initialized after it was created."""


class ServiceConfigurationError(RuntimeError):
    """An error during services configuration or initialization."""


class ServiceNotAvailableError(KeyError):
    """Service with such name doesn't exists."""


class ServiceClassRegistry(AbstractClassRegistry):
    """Class registry for service classes."""

    base_classes = [Service]


service_class_registry = ServiceClassRegistry(raise_if_exists=False)  #: default service class registry object


class ServiceContextManager(Service):
    """
    App cleanup ctx initialization for contextable services from a config list.

    :param app: aiohttp web application
    :param settings: service settings list in order in which they will be
        initialized on app start, settings must be compatible with
        the `ServiceSettings` interface
        You can pass an ordered dictionary if you want, the keys will
        be ignored.
    :param class_registry: you may provide a custom instance of class registry,
        see :class:`.AbstractClassRegistry` for details
    :param logger: a logger instance (None for default)
    """

    base_classes = [Service]
    service_name = 'services'
    DEFAULT_ENABLE_POLICY = True
    DEFAULT_REQUIRE_POLICY = True
    DEFAULT_REGISTER_IN_APP_POLICY = False
    DEFAULT_REGISTER_IN_MANAGER_POLICY = True
    service_class = Service
    contextable_service_class = Contextable
    service_of_services_class = ServiceOfServices

    def __init__(
            self, app: App, settings: Union[Iterable, OrderedDict],
            class_registry: ServiceClassRegistry = service_class_registry,
            auto_register_in_rpc_server=True, rpc_server_name='rpc', logger=None):
        super().__init__(app=app, logger=logger)
        self._auto_register_in_rpc_server = bool(auto_register_in_rpc_server)
        self._rpc_server_name = rpc_server_name
        self._class_registry = class_registry
        self._set_app_attrs(app, self.service_name, self)
        self._run_configurations = []
        self._services = {}
        self._init_services(settings)
        self.initialized = asyncio.Event()

    def keys(self):
        return list(key for key, value in self._services.items() if value is not None)

    def __contains__(self, item):
        """Checks if service with such name exists."""

        return item in self._services and self._services[item] is not None

    def __getitem__(self, item) -> Service:
        """Returns a service instance by its name.

        .. attention::

            A returned service doesn't always mean that it is ready to use,
            because its initialization may occur only after the app started.

        """

        if item in self:
            return self._services[item]
        else:
            raise ServiceNotAvailableError(
                'Service "%s" is not currently available.'
                'Available services: %s.'
                % (item, list(self.keys())))

    def get(self, item) -> Optional[Service]:
        """Same as __getitem__ but returns none if an item doesn't exist."""

        if item in self:
            return self[item]

    def __getattr__(self, item):
        if item in self:
            return self[item]
        else:
            return super().__getattribute__(item)

    def __len__(self):
        return len(self.keys())

    def __iter__(self):
        """Yield service contexts."""

        async def _terminate(app, service, config):
            self.logger.debug(
                'Closing "%s" service context.',
                config.cls)
            try:
                await service.close()
            except Exception as e:
                self.logger.error(
                    'Error closing "%s" service context. [%s]: %s',
                    config.cls, e.__class__.__name__, e)
            finally:
                if config.name in self._services:
                    del self._services[config.name]
                if config.name in app:
                    del app[config.name]
                if hasattr(app, config.name):
                    delattr(app, config.name)

        async def _self_ctx(app):
            self._set_app_attrs(app, self.service_name, self)
            self.logger.info(
                'Mapped a new service context manager "%s" -> "app.%s".',
                self.__class__.__name__, self.service_name)
            yield
            self._set_app_attrs(app, self.service_name, None)

        async def _set_event_ctx(app):
            self.initialized.set()
            yield

        async def _service_ctx(app, config: ServiceSettings):
            self.logger.debug('Initializing service "%s".', config.name)
            service = self._services[config.name]

            if isinstance(service, self.contextable_service_class):
                try:
                    self.logger.debug('Calling "%s" service context.', config.name)
                    await service.init()
                except InvalidLicense as e:
                    self.logger.error('InvalidLicense: %s', e.message)
                    await _terminate(app, service, config)
                    raise e

                except Exception as e:
                    self.logger.error(
                        'Error initializing "%s" service context. [%s]: %s',
                        config.cls, e.__class__.__name__, e)
                    await _terminate(app, service, config)
                    if config.required:
                        raise e
                else:
                    if config.register_in_manager is False:
                        del self._services[config.name]

            yield

            if service:
                if isinstance(service, self.contextable_service_class):
                    await _terminate(app, service, config)

        self.initialized.clear()

        yield _self_ctx

        for config in self._run_configurations:
            config = partial(_service_ctx, config=config)
            yield config

        yield _set_event_ctx

    def register_service(self, service: Service):
        service_name = getattr(service, 'service_name', None)
        if not service_name:
            service_name = service.__class__.__name__
        if service_name in self._services:
            raise RuntimeError('Service object with name "%s" is already registered.' % service_name)
        self._services[service_name] = service

    def discover_service(
            self, name: Union[str, Service] = None,
            cls: Union[Union[str, Type[Service]], Iterable[Union[str, Type[Service]]]] = None,
            required: bool = True
    ):
        """
        This method will try to discover a service using specified name and/or service
        class.

        :param name: specify a service name or service instance (in latter case
            it will be returned as is)
        :param cls: specify service class or a list of classes. If name wasn't specified,
            then the first service matching given class will be returned. If name and class
            both were specified, then the type check will be performed on a newly
            discovered service. If multiple classes are provided they will be checked in
            priority order one by one.
        :param required: means that an exception will rise if service doesn't exist
            otherwise in this case None will be returned
        """

        service = None

        if isinstance(name, self.service_class):
            return name

        if name:
            service = self._services.get(name)
            if cls and service and not isinstance(service, cls):
                raise TypeError(
                    'Service "%s" was discovered but it\'s not a subclass of "%s".'
                    ' Either set "key=None" to avoid this check or set "value=None"'
                    ' to get a default service of provided class.' % (service, cls))

        elif cls:
            if not isinstance(cls, Iterable):
                cls = [cls]
            for c in cls:
                if type(c) is str:
                    c = service_class_registry[c]
                service = next((
                    service for service in self._services.values()
                    if isinstance(service, c)), None)
                if service is not None:
                    break
        else:
            raise ValueError('At least one argument must be provided.')

        if service is None:
            if required:
                raise KeyError(
                    'Service "%s" of class "%s" doesn\'t exist.'
                    % (name, cls))
            else:
                self.logger.warning(
                    'Service dependence "%s" of class "%s" doesn\'t exist.',
                    name, cls)

        return service

    @staticmethod
    def _set_app_attrs(app, service_name, service):
        if app:
            app[service_name] = service
            setattr(app, service_name, service)

    def _init_services(self, settings: Union[List[dict], Dict[str, dict]]):
        if isinstance(settings, dict):
            settings = list(settings.values())
        for params in settings:
            self._init_service(params)

    def _init_service(self, params):

        from kaiju_tools.rpc.abc import AbstractRPCCompatible

        if isinstance(params, str):
            params = {'cls': params}

        try:
            cls = params['cls']
        except KeyError:
            raise ServiceConfigurationError("'cls' parameter must present in service configuration.")

        self.logger.debug('Trying to create service of type "%s".', cls)
        if cls not in self._class_registry:
            raise ServiceConfigurationError(
                'Service class "%s" is not registered. You need to register service class'
                ' in the ServiceClassRegistry and then pass this registry to the'
                ' ServiceContextManager on init.' % cls)
        cls = self._class_registry[cls]

        if issubclass(cls, AbstractRPCCompatible) and self._auto_register_in_rpc_server:
            register_in = params.get('register_in_services', [])
            if isinstance(register_in, str):
                register_in = [register_in]
            register_in.append(self._rpc_server_name)
            params['register_in_services'] = register_in

        self.logger.debug('Initializing "%s" service settings.', cls)

        if hasattr(cls, 'service_name') and 'name' not in params:
            params['name'] = cls.service_name

        try:
            run_configuration = ServiceSettings(**params)
        except Exception:
            raise ServiceConfigurationError(
                'Can\'t initialize service settings for a class "%s".' % cls)

        if run_configuration.enabled:
            self.logger.debug('Initializing service "%s".' % run_configuration.name)
            if run_configuration.name in self._services:
                raise ServiceConfigurationError(
                    'Conflict: service with name "%s" is registered twice.'
                    % run_configuration.name)
            service_settings = run_configuration.settings
            try:
                service = cls(app=self.app, logger=self.logger, **service_settings)
            except Exception:
                raise ServiceConfigurationError(
                    'Can\'t initialize service "%s": invalid service configuration.'
                    % run_configuration.name)

            service.service_name = run_configuration.name
            self._services[run_configuration.name] = service
            self._run_configurations.append(run_configuration)

            if run_configuration.register_in_services:
                for super_service in run_configuration.register_in_services:
                    self.logger.debug(
                        'Trying to register a new service "%s" in'
                        ' other service "%s".'
                        % (run_configuration.name, super_service))
                    if super_service in self._services:
                        super_service = self._services[super_service]
                        if isinstance(super_service, self.service_of_services_class):
                            super_service.register_service(run_configuration.name, service)
                        else:
                            raise ServiceConfigurationError(
                                'Other service "%s" must be an instance of `ServiceOfServices`'
                                'class. You need to change "register_in_services" config parameter'
                                'for service "%s".'
                                % (super_service, run_configuration.name))
                    else:
                        raise ServiceConfigurationError(
                            'Other service "%s" doesn\'t exist. You need to change'
                            ' "register_in_services" parameter for service "%s".'
                            % (super_service, run_configuration.name))

        else:
            self.logger.info('Service "%s" is disabled.' % run_configuration.name)
            service = None

        if run_configuration.register_in_app:
            self._set_app_attrs(self.app, run_configuration.name, service)
            if service:
                self.logger.info(
                    'Mapped a new service "%s" -> "app.%s.%s".',
                    run_configuration.cls, self.service_name,
                    run_configuration.name)

        self._services[run_configuration.name] = service

        return service


class ServiceSettings(Serializable):
    """
    Service settings specification.

    Because settings class inherits from :class:`.Serializable`, it means, that
    it can be easily converted to/from `dict` or json.

    :param cls: service class name
    :param name: service custom name
        if None, then it is defined by the algorithm: i.e. if the service
        has `service_name` set, then `service_name` will be used as service name.
        If `service_name` is also None, then `__name__` of the service class
        will be used
    :param info: human readable information about the service
    :param enabled: if False, then service initialization will be skipped
    :param required: a required service means that the app won't start if it fails
    :param register_in_app: a registered service means that it will be added to
        the application dictionary and attributes
    :param register_in_services: perform a registration of a service in other service(s)
    :param register_in_manager:
    :param settings: service custom settings
    """

    __slots__ = (
        'cls', 'name', 'info', 'enabled', 'required', 'settings',
        'register_in_services', 'register_in_app', 'register_in_manager'
    )

    def __init__(
            self, cls: str, name: str = None, info: str = None,
            enabled: bool = None, required: bool = None, register_in_app: bool = None,
            settings: dict = None, register_in_services: Union[str, List[str]] = None,
            register_in_manager: bool = None):

        self.cls = cls

        if name:
            self.name = name
        else:
            self.name = cls

        if info is not None:
            self.info = info
        else:
            self.info = ''

        if enabled is not None:
            self.enabled = enabled
        else:
            self.enabled = ServiceContextManager.DEFAULT_ENABLE_POLICY

        if register_in_app is not None:
            self.register_in_app = register_in_app
        else:
            self.register_in_app = ServiceContextManager.DEFAULT_REGISTER_IN_APP_POLICY

        if required is not None:
            self.required = required
        else:
            self.required = ServiceContextManager.DEFAULT_REQUIRE_POLICY

        if settings is not None:
            self.settings = settings
        else:
            self.settings = {}

        if register_in_services is not None:
            if isinstance(register_in_services, str):
                self.register_in_services = frozenset([register_in_services])
            else:
                self.register_in_services = frozenset(register_in_services)
        else:
            self.register_in_services = []

        if register_in_manager is not None:
            self.register_in_manager = register_in_manager
        else:
            self.register_in_manager = ServiceContextManager.DEFAULT_REGISTER_IN_MANAGER_POLICY

    def repr(self):
        return {
            'cls': self.cls,
            'name': self.name,
            'info': self.info,
            'enabled': self.enabled,
            'register_in_app': self.register_in_app,
            'required': self.required,
            'register_in_manager': self.register_in_manager,
            'register_in_services': self.register_in_services,
            'settings': self.settings
        }
