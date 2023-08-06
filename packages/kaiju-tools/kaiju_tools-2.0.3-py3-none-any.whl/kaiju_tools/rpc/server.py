"""
RPC server implementation.

Request headers
---------------

Supported request headers:

- **X-Request-Deadline** - absolute request deadline in UNIX timestamp format.
    If a request exceeds this deadline it will be aborted by the server
- **X-Request-Timeout** - max request exec time in seconds since it was accepted by a server
- **X-App-ID** - your application unique ID, should be an UUID string
- **X-Correlation-ID** - request correlation ID, all requests actually are being
    cached by (X-App-ID, X-Correlation-ID) key, so this parameter is important.
    It should be an UUID string.
- **Content-Type** - content mimetype, application/json etc.

.. note::

    The difference between *X-Correlation-ID* and *id* of a JSON RPC request is
    that id is used to identify a specific request in a batch, and correlation
    id is used to identify a message amongst other messages sent to a server.

See AD for more info about how all headers are processed by the server.

.. image:: ../images/RPCRequestHeadersProcessing.png


Supported content types
-----------------------

Currently only *application/json* is supported.


Performance
-----------

Performance is checked on simple requests with random request ids, where
an rpc function only echoes a request back to the client.

.. code-block::

    Test results (best of 3)
    Intel(R) Core(TM) i5-7360U CPU @ 2.30GHz
    Python 3.8.1
    2020-01-24

    asyncio

    16 connections
    0:00:00.302650
    6208 requests
    20512.1 req/sec

    uvloop

    16 connections
    0:00:00.199588
    5200 requests
    26053.6 req/sec


Classes
-------

"""

import abc
import asyncio
import bisect
import inspect
import string
from collections import namedtuple
from time import time
from uuid import uuid4, UUID
from collections import ChainMap
from dataclasses import dataclass, asdict
from textwrap import dedent
from traceback import print_tb
from typing import *

try:
    from typing import TypedDict
except ImportError:
    # python 3.6 compatibility
    from typing_extensions import TypedDict

import fastjsonschema

from kaiju_tools.serialization import Serializable
from . import jsonrpc
from .abc import AbstractRPCCompatible, PermissionKeys, Session, ServerSessionFlag
from .etc import JSONRPCHeaders
from .client import AbstractRPCTransportInterface
from ..exceptions import APIException, ValidationError, ensure_traceback
from ..services import ContextableService, ServiceOfServices
from ..jsonschema import compile_schema, JSONSchemaObject, Integer, String, GUID, Object, Constant

__all__ = (
    'RequestHeaders', 'rpc_service_config', 'QueuedRequest',
    'AbstractJSONRPCInterface', 'JSONRPCServer'
)


class RequestHeaders(TypedDict):
    """Expected request headers dict."""

    APP_ID_HEADER: Optional[UUID]
    CORRELATION_ID_HEADER: Optional[UUID]
    REQUEST_DEADLINE_HEADER: Optional[int]
    REQUEST_TIMEOUT_HEADER: Optional[int]


rpc_service_config = {
    'cls': 'JSONRPCServer',
    'name': 'rpc',
    'info': 'RPC server',
    'register_in_app': True,
    'settings': {
        'max_request_time': 60,
        'default_request_time': 10,
        'request_queue_size': 512,
        'response_queue_size': 256,
        'max_parallel_tasks': 16
    }
}  # example of a service manager configuration


QueuedRequest = namedtuple('QueuedRequest', 'headers data session callback') #: you can use it to put data to the requests queue of a server


class AbstractJSONRPCInterface(abc.ABC):
    """
    Interface class manages RPC methods and namespaces registration.

    :param server_id: server id (used in response headers)
    :param max_request_time: maximum request time in sec for any request
    :param default_request_time: default request time in sec
    :param system_permission_key: system permission (all methods are allowed)
    :param guest_permission_key: guest user permission (all users allowed)
    """

    @dataclass(frozen=True)
    class RequestHeaders:
        app_id: str
        correlation_id: str
        deadline: int
        extras: dict

    server_methods_namespace = 'server'
    rpc_compatible_classes = (AbstractRPCCompatible, )
    SESSION_ARG_KEY = 'session'  #: RPC methods starting with this arg will automatically get a session dict
    HEADERS_ARG_KEY = '_headers'  #: RPC methods using header arg will automatically get a request headers dict
    SYSTEM_PERMISSION = PermissionKeys.GLOBAL_SYSTEM_PERMISSION
    GUEST_PERMISSION = PermissionKeys.GLOBAL_GUEST_PERMISSION

    MAX_REQUEST_TIME = 60
    DEFAULT_REQUEST_TIME = 1

    def __init__(
            self,
            server_id: UUID,
            max_request_time: int = MAX_REQUEST_TIME,
            default_request_time: int = DEFAULT_REQUEST_TIME,
            system_permission_key: str = SYSTEM_PERMISSION,  # not used anymore
            guest_permission_key: str = GUEST_PERMISSION
    ):

        self._server_id = str(server_id) if server_id else str(uuid4())
        self._system_permission_key = PermissionKeys.GLOBAL_SYSTEM_PERMISSION
        self._guest_permission_key = guest_permission_key
        self._max_request_time = max(1, max_request_time)
        self._default_request_time = min(max(1, default_request_time), max_request_time)
        self._default_system_permissions = frozenset({self._system_permission_key})

        self._namespaces = {}
        self._permissions = {}
        self._validators = {}
        self._f_awaitable = {}
        self._f_sync = {}
        self._require_session = set()
        self._require_headers = set()
        self._methods = ChainMap(self._f_awaitable, self._f_sync)

        self.register_namespace(
            self.server_methods_namespace,
            {
                'settings': self.list_settings,
                'schema': self.get_spec
            },
            permissions={
                AbstractRPCCompatible.DEFAULT_PERMISSION: self._system_permission_key
            },
            validators={}
        )

    def list_settings(self):
        return {
            'server_id': self._server_id,
            'max_request_time': self._max_request_time,
            'default_request_time': self._default_request_time
        }

    def get_spec(self):
        data = list(self._methods.keys())
        data.sort()
        return data

    def register_namespace(self, namespace: str, routes: dict, permissions: dict, validators: dict):
        """Registers a new namespace with RPC methods."""

        def _parse_permissions(_permissions):
            default_permission = _permissions.get(AbstractRPCCompatible.DEFAULT_PERMISSION)
            wildcards, keys = {}, {}
            for key, value in _permissions.items():
                if key != AbstractRPCCompatible.DEFAULT_PERMISSION:
                    if key.endswith('*') or key.startswith('*'):
                        wildcards[key] = value
                    else:
                        keys[key] = value
            return default_permission, wildcards, keys

        def _check_method_permissions(method_name, default_permission, wildcards, keys):
            if method_name in keys:
                permission = keys[method_name]
            else:
                for key, value in wildcards.items():
                    if key.startswith('*'):
                        key = key.lstrip('*')
                        if method_name.endswith(key):
                            permission = value
                            break
                    elif key.endswith('*'):
                        key = key.rstrip('*')
                        if method_name.startswith(key):
                            permission = value
                            break
                else:
                    permission = default_permission
            return permission

        namespace = self._strip_key(namespace)
        if namespace in self._namespaces:
            _namespace = self._namespaces[namespace]
        else:
            _namespace = self._register_namespace(namespace)

        default_permission, wildcards, keys = _parse_permissions(permissions)
        for method_name, func in routes.items():
            validator = validators.get(method_name)
            method_name = self._strip_key(method_name)
            permission = _check_method_permissions(
                method_name, default_permission, wildcards, keys)
            if method_name in _namespace:
                raise ValueError(
                    'RPC method "%s" is already registered in namespace "%s".'
                    % (method_name, namespace))

            method_name = f'{namespace}.{method_name}'
            self._register_method(method_name, func)

            _namespace.add(method_name)
            if permission:
                self._permissions[method_name] = permission

            if validator:
                self._validators[method_name] = AbstractRPCCompatible._compile_schema(validator)

    def register_service(self, service_name: str, service: AbstractRPCCompatible):
        """
        Registers an RPC compatible service.
        Basically it is an alias to the `register_namespace` method.
        """

        if not isinstance(service, self.rpc_compatible_classes):
            raise TypeError(
                'Incompatible service %s with name %s. Must be an instance of'
                ' `AbstractRPCCompatible`.' % (service, service_name))

        self.register_namespace(service_name, service.routes, service._permissions_wrapper(), service.validators)

    def _register_namespace(self, namespace: str) -> set:
        if namespace.lower() == 'rpc':
            raise ValueError(
                'Namespace "rpc" is reserved for system methods'
                ' by the JSON RPC 2.0 specification.')
        elif not namespace:
            raise ValueError('Empty or non-alphanumeric namespaces are not allowed.')
        elif namespace in self._namespaces:
            raise ValueError('RPC namespace "%s" is already registered.' % namespace)
        else:
            self._namespaces[namespace] = _namespace = set()
            return _namespace

    def _register_method(self, name: str, func: Callable):

        if name in self._methods:
            raise RuntimeError('Method with the name "%s" can\'t be registered twice.' % name)

        if inspect.iscoroutinefunction(func):
            self._f_awaitable[name] = func
        else:
            self._f_sync[name] = func

        args = inspect.signature(func).parameters
        if args:
            if self.SESSION_ARG_KEY in args:
                self._require_session.add(name)
            if self.HEADERS_ARG_KEY in args:
                self._require_headers.add(name)

    @staticmethod
    def _strip_key(key: str):
        key = key.strip(string.punctuation + string.whitespace)
        return key

    def _process_request_headers(self, headers: Optional[dict]) -> RequestHeaders:
        """Request headers processing and validation."""

        if headers is None:
            headers = {}

        t = int(time()) + 1

        # request deadline calculation

        deadline = headers.pop(JSONRPCHeaders.REQUEST_DEADLINE_HEADER, None)
        timeout = headers.pop(JSONRPCHeaders.REQUEST_TIMEOUT_HEADER, None)
        try:
            deadline = int(deadline)
        except (ValueError, TypeError):
            deadline = None
        try:
            timeout = int(timeout)
        except (ValueError, TypeError):
            timeout = None
        if deadline:
            deadline = min(self._max_request_time + t, deadline)
        if timeout:
            timeout = min(self._max_request_time, timeout)
            _deadline = t + timeout
            if not deadline or _deadline < deadline:
                deadline = _deadline
        if not deadline:
            deadline = t + self._default_request_time

        # request and app identifiers

        correlation_id = headers.pop(JSONRPCHeaders.CORRELATION_ID_HEADER, None)
        if correlation_id:
            correlation_id = correlation_id if type(correlation_id) is UUID else UUID(correlation_id)
        else:
            correlation_id = uuid4()

        app_id = headers.pop(JSONRPCHeaders.APP_ID_HEADER, None)
        if app_id:
            app_id = app_id if type(app_id) is UUID else UUID(app_id)
        else:
            app_id = uuid4()

        return self.RequestHeaders(app_id, correlation_id, deadline, extras=headers)

    def _process_response_headers(self, headers: Optional[RequestHeaders], **extras):
        if headers:
            return {
                JSONRPCHeaders.APP_ID_HEADER: str(headers.app_id),
                JSONRPCHeaders.CORRELATION_ID_HEADER: str(headers.correlation_id),
                JSONRPCHeaders.SERVER_ID_HEADER: self._server_id,
                **extras
            }
        else:
            return {
                JSONRPCHeaders.SERVER_ID_HEADER: self._server_id,
                **extras
            }


class JSONRPCServer(ContextableService, AbstractJSONRPCInterface, ServiceOfServices, AbstractRPCTransportInterface):
    """A simple JSON RPC interface with method execution and management tasks.

    :param app: optional web application instance
    :param max_request_time: maximum request time in sec for any request
    :param default_request_time: default request time in sec
    :param deadline_check_interval: dead requests checker interval
    :param debug: debug mode, if None then app.debug will be used
    :param request_queue_size: max number of awaiting requests
    :param response_queue_size: max number of prepared and not sent responses
    :param remove_responses_on_overflow:
    :param max_parallel_tasks: max number of tasks executing in parallel
    :param logger: optional logger instance
    """

    service_name = 'rpc'

    # default queue / execution settings

    DEADLINE_CHECK_INTERVAL = 1
    REQUEST_QUEUE_SIZE = 256
    RESPONSE_QUEUE_SIZE = 1000
    RESPONSE_QUEUE_CHECK_INTERVAL = 0.5
    REMOVE_RESPONSES_ON_OVERFLOW = True
    MAX_PARALLEL_TASKS = 8

    # other defaults

    MAX_REQUEST_TIME = AbstractJSONRPCInterface.MAX_REQUEST_TIME
    DEFAULT_REQUEST_TIME = AbstractJSONRPCInterface.DEFAULT_REQUEST_TIME
    SESSION_ARG_KEY = AbstractJSONRPCInterface.SESSION_ARG_KEY
    SYSTEM_PERMISSION = AbstractJSONRPCInterface.SYSTEM_PERMISSION
    GUEST_PERMISSION = AbstractJSONRPCInterface.GUEST_PERMISSION

    _zero_length_exception = ValueError('Batch of length 0 received.')

    def __init__(
            self, app=None,

            deadline_check_interval: int = DEADLINE_CHECK_INTERVAL,
            request_queue_size: int = REQUEST_QUEUE_SIZE,
            response_queue_size: int = RESPONSE_QUEUE_SIZE,
            response_queue_check_interval: int = RESPONSE_QUEUE_CHECK_INTERVAL,
            remove_responses_on_overflow: bool = REMOVE_RESPONSES_ON_OVERFLOW,
            max_parallel_tasks: int = MAX_PARALLEL_TASKS,

            max_request_time: int = MAX_REQUEST_TIME,
            default_request_time: int = DEFAULT_REQUEST_TIME,
            system_permission_key: str = SYSTEM_PERMISSION,
            guest_permission_key: str = GUEST_PERMISSION,

            debug: bool = None, logger=None
    ):

        AbstractJSONRPCInterface.__init__(
            self,
            server_id=getattr(app, 'id', None),
            max_request_time=max_request_time,
            default_request_time=default_request_time,
            system_permission_key=system_permission_key,
            guest_permission_key=guest_permission_key)
        ContextableService.__init__(self, app=app, logger=logger)

        # settings

        self._deadline_check_interval = max(0, deadline_check_interval)
        self._debug = self.app.debug if self.app and debug is None else bool(debug)
        self._max_parallel_tasks = max(1, max_parallel_tasks)
        self._request_queue_size = max(0, request_queue_size)
        self._response_queue_size = max(0, response_queue_size)
        self._remove_responses_on_overflow = bool(remove_responses_on_overflow)
        self._response_queue_check_interval = max(0, response_queue_check_interval)

        # request and tasks related stuff

        self._closed = True
        self.requests = None   # awaiting requests
        self._responses = None  # awaiting responses
        self._tasks = {}  # map of currently ongoing tasks
        self._deadline_ids = []  # task ids related to deadlines list
        self._deadlines = []     # task deadlines in asc order
        self._deadline_monitor = None  # looping task what checks for other task deadlines
        self._workers = None     # list of request processing tasks
        self._response_queue_worker = None

    async def init(self):
        self.logger.info('Starting.')
        self._closed = False

        self.logger.debug('Starting deadline monitor.')
        self._deadline_monitor = asyncio.ensure_future(self._check_queue_ttl())

        self.logger.debug('Initializing a request queue.')
        self.requests = asyncio.Queue(maxsize=self._request_queue_size)
        self._responses = asyncio.Queue(maxsize=self._response_queue_size)

        self.logger.debug('Starting %d parallel workers.' % self._max_parallel_tasks)
        self._workers = [
            asyncio.ensure_future(self._worker())
            for _ in range(self._max_parallel_tasks)
        ]

        self._response_queue_worker = asyncio.ensure_future(self._response_loop())

        await super().init()
        self.logger.info('Started.')

    async def close(self):
        self._closed = True
        self.logger.info('Closing.')

        if self.requests is not None:
            self.logger.debug('Processing %d requests left in the queue.' % self.requests.qsize())
            await self.requests.join()
            self.requests = None

        if self._tasks is not None:
            self.logger.debug('Awaiting %d request tasks.' % len(self._tasks))
            await asyncio.gather(
                *(task for task in self._tasks.values()),
                return_exceptions=True)

        if self._workers is not None:
            self.logger.debug('Stopping request workers.')
            for worker in self._workers:
                worker.cancel()
            self._workers = None

        if self._response_queue_worker is not None:
            self._response_queue_worker.cancel()
        self._responses = None

        self._tasks, self._deadlines = {}, {}
        self.logger.debug('Stopping deadline monitor.')
        self._deadline_monitor.cancel()
        self._deadline_monitor = None
        await super().close()
        self.logger.info('Closed.')

    @property
    def closed(self):
        return self._closed

    async def get_spec(self) -> dict:
        services = []
        info = {
            'jsonrpc': '2.0',
            'rpcapi': '0.1.0',
            'info': {
                'name': self.app.name,
                'version': self.app.version,
                'description': f'{self.app.name} public API'
            },
            'servers': [
                {
                    'name': 'local',
                    'description': 'local test server',
                    'url': f'http://localhost:{self.app.settings["run"]["port"]}/public/rpc',
                    'auth': [
                        {
                            'type': 'jwt',
                            'getMethod': 'auth.jwt_get',
                            'refreshMethod': 'auth.jwt_refresh'
                        }
                    ]
                }
            ],
            'requestHeaders': [
                Object({
                    'Content-Type': Constant(
                        'application/json',
                        description='Request body content type.'
                    ),
                    'X-Request-Timeout': Integer(
                        description='Max request time in seconds.',
                        minimum=0,
                        maximum=self._max_request_time,
                        default=self._default_request_time
                    )
                })
            ],
            'responseHeaders': [],
            'errors': [],
            'services': services
        }
        for service_name, service in self.app.services._services.items():
            if isinstance(service, AbstractRPCCompatible):
                service_info = {
                    'name': service_name
                }
                doc = service.__doc__
                if doc:
                    service_info['description'] = dedent(doc)
                service_info['methods'] = service_methods = []
                for method_name, method in service.routes.items():
                    full_method_name = f'{service_name}.{method_name}'
                    if full_method_name in self._methods:
                        permission = self._permissions.get(full_method_name)
                        validator = service.validators.get(method_name)
                        result = service.responses.get(method_name)
                        auth = service.has_permission({'permissions': {self._guest_permission_key}}, permission)
                        doc = method.__doc__
                        method = {
                            'name': full_method_name,
                            'authRequired': auth,
                            'requestHeaders': [],
                            'responseHeaders': [],
                            'errors': []
                        }
                        if doc:
                            method['description'] = dedent(doc)
                        if validator and isinstance(validator, JSONSchemaObject):
                            method['params'] = validator.repr()
                        if result:
                            method['result'] = result.repr()
                        service_methods.append(method)

                services.append(service_info)

        services.sort(key=lambda o: o['name'])
        return info

    async def rpc_request(
            self, uri: str,
            request: Union[jsonrpc.RPCRequest, List[jsonrpc.RPCRequest]],
            headers: Optional[Dict[str, Any]]) -> Union[dict, list]:
        """Temporary compatibility with an rpc client."""

        _h, data = await self.call(data=request, headers=headers)
        return data

    async def call(self, data: Union[List, Dict], headers: RequestHeaders = None, session: Session = None):
        """
        Request with a callback. This will eventually return the result.

        :param data: request body
        :param headers: request headers (optional)
        :param session: user session data (optional)
        """

        callback = asyncio.Queue()
        await self.requests.put((headers, data, session, callback))
        result = await callback.get()
        if result:
            headers, data = result
            return headers, data

    async def _response_loop(self):
        response_queue = self._responses
        response_queue_check_interval = self._response_queue_check_interval
        sleep = asyncio.sleep

        while 1:
            q = response_queue.qsize()
            if q:
                for _ in range(q):
                    headers, data, callback = response_queue.get_nowait()
                    response_queue.task_done()
                    if callback.full():
                        response_queue.put_nowait((headers, data, callback))
                    else:
                        callback.put_nowait((headers, data, callback))
            await sleep(response_queue_check_interval)

    async def _worker(self):
        request_queue = self.requests
        response_queue = self._responses
        flush_response_on_overflow = self._remove_responses_on_overflow
        _process_request_headers = self._process_request_headers
        _process_response_headers = self._process_response_headers
        _on_request = self._on_request
        zero_length_request_exc = jsonrpc.InvalidRequest(
            None, debug=self._debug, base_exc=self._zero_length_exception)

        while 1:

            headers, data, session, callback = await request_queue.get()

            try:

                req_headers = None

                if data:
                    try:
                        req_headers = _process_request_headers(headers)
                    except (ValueError, TypeError) as exc:
                        result = jsonrpc.InvalidRequest(
                            None, debug=self._debug, base_exc=exc)
                    else:
                        if type(data) is list:
                            result = await asyncio.gather(*(
                                _on_request(req_headers, session, kws)
                                for kws in data))
                            result = [r for r in result if r is not None]
                        else:
                            result = await _on_request(req_headers, session, data)
                else:
                    result = zero_length_request_exc

                if callback is not None:
                    resp_headers = _process_response_headers(req_headers)

                    if callback.full():
                        if response_queue.full():
                            if flush_response_on_overflow:
                                response_queue.get_nowait()
                                response_queue.task_done()
                                response_queue.put_nowait((resp_headers, result, callback))
                            else:
                                await response_queue.put((resp_headers, result, callback))
                        else:
                            response_queue.put_nowait((resp_headers, result, callback))
                    else:
                        callback.put_nowait((resp_headers, result))

            except Exception as exc:
                self._send_traceback(exc, headers, data)
            finally:
                request_queue.task_done()

    def _send_traceback(self, exc, headers=None, body=None):
        extra = {
            'fingerprint': ['rpc_server', body.get('method')],
            'capturer': 'rpc_server',
            'request': {
                'method': 'POST',
                'headers': headers,
                'body': body
            },
            'response': {}
        }
        if isinstance(exc, jsonrpc.RPCError):
            extra['response']['body'] = exc.repr()
            extra['response']['status'] = exc.code
            extra['fingerprint'].append(str(exc.code))
        else:
            extra['response']['body'] = str(exc)
        exc = ensure_traceback(exc)
        self.logger.exception(exc, extra=None, exc_info=(type(exc), exc, exc.__traceback__))

    async def _on_request(
            self, headers: RequestHeaders, session: Session,
            kws: dict) -> Union[jsonrpc.RPCResponse, jsonrpc.RPCError]:
        """Configured for both request object and json request body."""

        # initializing request object

        try:
            request = jsonrpc.RPCRequest(**kws)
        except TypeError as e:
            return jsonrpc.InvalidRequest(kws.get('id'), base_exc=e)

        if headers.deadline < time():
            return jsonrpc.RequestTimeout(request.id)

        request_method = request.method

        try:
            method = self._methods[request_method]
        except KeyError:
            return jsonrpc.MethodNotFound(request.id, data={'method': request_method})

        # checking permissions

        if session:
            if session == ServerSessionFlag:
                permissions = self._default_system_permissions
                session = {'permissions': permissions}
            else:
                permissions = session.get('permissions', set())
        else:
            permissions = {self._guest_permission_key}
            session = {'permissions': permissions}

        if self._system_permission_key not in permissions:
            permission_key = self._permissions.get(request_method, self._system_permission_key)
            if permission_key != self._guest_permission_key and permission_key not in permissions:
                if session.get('user_id'):
                    return jsonrpc.PermissionDenied(request.id, data={'method': request_method})
                else:
                    return jsonrpc.NotAuthorized(request.id, data={'method': request_method})

        # awaiting task

        task = None
        app_id = headers.app_id
        correlation_id = headers.correlation_id

        if request.id:
            _id = (app_id, correlation_id, request.id)
            if _id in self._tasks:
                task = self._tasks[_id]
        else:
            _id = (app_id, correlation_id, uuid4().int)

        try:

            if not task:
                request_params = request.params

                if request_params is None:
                    request_params = {}

                # validating input parameters

                if request_method in self._validators:
                    try:
                        validator = self._validators[request_method]
                        for v_func in validator:
                            request_params = v_func(request_params)
                    except fastjsonschema.JsonSchemaException as exc:
                        return jsonrpc.InvalidParams(
                            id=request.id, base_exc=exc, data={'method': request_method},
                            debug=self._debug)
                    except ValidationError as exc:
                        return jsonrpc.InvalidParams.from_api_exception(
                            id=request.id, exc=exc, data={'method': request_method},
                            debug=self._debug)

                # exec

                try:
                    if request_method in self._require_session:
                        request_params[self.SESSION_ARG_KEY] = session
                    if request_method in self._require_headers:
                        request_params[self.HEADERS_ARG_KEY] = asdict(headers)

                    if request_params:
                        result = method(**request_params)
                    else:
                        result = method()

                except TypeError as exc:
                    return jsonrpc.InvalidParams(
                        request.id, base_exc=exc, data={'method': request_method},
                        debug=self._debug)

                if request_method in self._f_awaitable:
                    self._tasks[_id] = result = asyncio.ensure_future(result)
                    self._deadline_ids.append(_id)
                    self._deadlines.append(headers.deadline)
                    result = await result
                    del self._tasks[_id]

            elif task.done():
                result = task.result()
                if _id in self._tasks:
                    del self._tasks[_id]
            else:
                result = await task
                if _id in self._tasks:
                    del self._tasks[_id]

        except asyncio.CancelledError:
            return jsonrpc.RequestTimeout(request.id)
        except APIException as exc:
            if self.app.debug:
                self._send_traceback(exc, headers, request.repr())
            return jsonrpc.RPCError.from_api_exception(
                id=request.id, exc=exc, data={'method': request_method},
                debug=self._debug)
        except jsonrpc.RPCError as exc:
            exc.id = request.id
            exc.debug = self._debug
            if self.app.debug:
                self._send_traceback(exc, headers, request.repr())
            return exc
        except Exception as exc:
            self._send_traceback(exc, headers, request.repr())
            return jsonrpc.InternalError(
                request.id, base_exc=exc, data={'method': request_method},
                debug=self._debug)
        else:
            if request.id is not None:
                return jsonrpc.RPCResponse(request.id, result=result)

    async def _check_queue_ttl(self):
        """
        Periodically checks awaiting requests for deadlines. Tasks exceeded
        their deadlines will be cancelled and removed.
        """

        check_interval = self._deadline_check_interval
        bisect_left = bisect.bisect_left

        while 1:
            if self._tasks:
                t = time()
                n = bisect_left(self._deadlines, t)

                if n:
                    for task_id, deadline in zip(self._deadline_ids[:n], self._deadlines[:n]):
                        if task_id in self._tasks:
                            task = self._tasks[task_id]
                            if not task.done():
                                task.cancel()
                            del self._tasks[task_id]

                    self._deadline_ids = self._deadline_ids[n:]
                    self._deadlines = self._deadlines[n:]

            await asyncio.sleep(check_interval)
