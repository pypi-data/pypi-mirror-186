"""Abstract RPC classes.

See :class:`.AbstractRPCCompatible` if you need to define an RPC compatible
interface.

Classes
-------

"""

import abc
import uuid
from inspect import iscoroutinefunction
from typing import Optional, TypedDict, Union, Dict, Any, List

from kaiju_tools.jsonschema import compile_schema
from . import jsonrpc

__all__ = (
    'AbstractRPCCompatible', 'PermissionKeys', 'Session', 'ServerSessionFlag',
    'AbstractRPCTransportInterface', 'AbstractTokenInterface'
)


class Session(TypedDict):
    """Expected session dict."""

    user_id: Optional[uuid.UUID]    #: user ID or None for guest and system accounts
    permissions: frozenset          #: map of user permissions
    stored: bool                    #: tells that this session is stateful and will be stored
    data: dict                      #: arbitrary user data


ServerSessionFlag = 'ON_SERVER'  #: this one's used to disable permission checks
# if you calling any function which requires a session arg directly from a server backed
# `AbstractRPCCompatible.has_permission` will always return true for this
# and `AbstractRPCCompatible.get_user_id` will return None


class PermissionKeys:
    """Standard useful permission keys."""

    GLOBAL_SYSTEM_PERMISSION = 'system'
    GLOBAL_USER_PERMISSION = 'user'
    GLOBAL_GUEST_PERMISSION = 'guest'


class AbstractRPCCompatible(abc.ABC):
    """
    An object compatible with the RPC interface.

    To be able to access methods you need to register your class in the RPC
    interface instance, and set routes and permissions (optional) values. See
    example below.

    .. code-block::python

        class MyRPCCompatible(AbstractRPCCompatible):

            async def do_something(self):
                return True

            @property
            def routes(self):
                return {
                    **super().routes,
                    "do": self.do_something
                }

            def permissions(self):
                return {
                    **super().permissions
                    "do": "custom_permission"
                }

    Use `DEFAULT_PERMISSION` permission key to specify permissions for all
    unmentioned methods.

    .. code-block::python

        class MyRPCCompatible(AbstractRPCCompatible):

            async def do_something(self):
                return True

            async def do_something_else(self):
                return False

            @property
            def routes(self):
                return {
                    **super().routes,
                    "do": self.do_something,
                    "do_2": self.do_something_else
                }

            def permissions(self):
                return {
                    **super().permissions,
                    self.DEFAULT_PERMISSION: "do_something"   #: both do and do_2 will use this permission by default
                }

    You can use simple wildcards for matching multiple permissions at once. If any
    method has explicit permission key then all wildcards will be ignored. See example.

    .. code-block::python

        class MyRPCCompatible(AbstractRPCCompatible):

            def permissions(self):
                return {
                    self.DEFAULT_PERMISSION: "p1",
                    "do.*": "p2",    # 'p2' permission will be used for all methods starting with 'do.'
                    "do.exit": "p3"  # 'do.exit' will specifically use 'p3' permission
                }

    :param permissions: it is now possible to pass custom permission map in settings
    """

    DEFAULT_PERMISSION = '*'
    PermissionKeys = PermissionKeys
    ServerSessionFlag = ServerSessionFlag

    def __init__(self, permissions: dict = None):
        self._permissions = permissions
        self._validators = self._compile_validators()

    @property
    def routes(self) -> dict:
        """
        A dictionary of a service RPC routes.

        Guides:

        - All enclosing punctuation, whitespaces will be stripped
        - RPC server usually will add a service prefix for each method, so if your service
          `service_name` is AwesomeService and your method route is `do_nothing` then an
          RPC client should call `AwesomeService.do_nothing`
        - Use simple *lowercased* method names
        - Use dots to separate logical sections (like "users." for user methods, "test." for test methods etc.)
        - If you inheriting and expanding an existing interface, try to inherit
          its routes as well (see example below)

        .. code-block:: python

            class MyService(MyOtherService):

                @property
                def routes(self) -> dict:
                    {
                      **super().routes,
                      "do_something": self.do_something_function,
                      "do_something_else": self.do_something_else_function
                    }

        """

        return {}

    @property
    def permissions(self) -> dict:
        """
        You may specify a custom set of permissions for certain routes. By default
        the permissions will be set to `None` which usually means that only the
        system user can access methods.

        You can redefine default permissions for all method using `DEFAULT_PERMISSION`
        key

        .. code-block:: python

            class MyService(AbstractRPCCompatible):

                @property
                def permissions(self) -> Optional[dict]:
                    return {
                        self.DEFAULT_PERMISSION: 'key_for_all_permissions'
                    }

        or you may provide a simple wildcard:

        .. code-block:: python

            class MyService(AbstractRPCCompatible):

                @property
                def permissions(self) -> Optional[dict]:
                    return {
                        self.DEFAULT_PERMISSION: 'key_for_all_permissions',
                        'users.*': 'key_for_all_user_methods_is_different'
                    }

        or explicitly set permissions for specific method names

        .. code-block:: python

            class MyService(AbstractRPCCompatible):

                @property
                def permissions(self) -> Optional[dict]:
                    return {
                        self.DEFAULT_PERMISSION: 'key_for_all_permissions',
                        'users.*': 'key_for_all_user_methods_is_different',
                        'users.destroy': 'this_permission_is_unique_for_a_single_method',
                        'users.kill': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION,      # this one will be system
                        'users.do_nothing': self.PermissionKeys.GLOBAL_GUEST_PERMISSION  # this one will be for guests
                    }

        Permissions are resolved in such order:

        1. Unique permission that matches given name exactly
        2. Wildcards starting or ending with '*' in order they are listed in the mapping
        3. Default permission
        4. System permission if default is not set

        """

        return {}

    def _permissions_wrapper(self) -> dict:
        """Used by a JSON RPC server to get permissions."""

        permissions = self.permissions
        custom_permissions = getattr(self, '_permissions', None)
        if custom_permissions:
            permissions.update(custom_permissions)
        return permissions

    @property
    def validators(self) -> dict:
        """
        Maps method routes to validator schemas. The schemas will be automatically
        compiled on RPC server start.

        .. attention::

            These validators are not used by services themselves, because there is
            no need for redundant validation on backend. Validators are used only
            when accessing a method via an RPC server. Thus you should only use
            validators to ensure the client data is of correct type, format or
            size.

        Example of use.

        .. code-block:: python

            class MyService(AbstractRPCCompatible):

                @property
                def routes(self):
                    return {
                        'run': self.my_function
                    }

                @property
                def validators(self):
                    return {
                        'run': Object({'value': Integer(minimum=41)})
                    }

                def my_function(self, value):
                    return value ** 2

        Or you can use your own callable as validator (although the jsonschema
        can be compiled and thus it's usually faster). Your validator MUST be
        a callable with a single positional dict argument (i.e. request params).

        .. code-block:: python

            @property
            def validators(self):
                return {
                    'run': self.custom_validator
                }

            def custom_validator(self, data):
                if type(value) is not int or value < 41:
                    raise ValidationError('Value is bad.')

        There's also a support for both function and schema with an arbitrary validation order:

        .. code-block:: python

            @property
            def validators(self):
                return {
                    'run': {
                      'schema': Object({'value': Integer(minimum=41)}),
                      'function': self.custom_validator,
                      'call_before_schema': True  # tells an RPC server that the schema must be called after the func
                    }
                }

        """

        return {}

    @property
    def responses(self) -> dict:
        """Here you may define the response schema for your public RPC methods."""
        return {}

    async def validate(self, method: str, data):
        """
        Validate method params using an internal validator schema.

        :returns: may return a normalized data object
        """
        validators = self._validators.get(method)
        if validators:
            for validator in self._validators[method]:
                data = validator(data)
                if iscoroutinefunction(validator):
                    data = await data
        return data

    @staticmethod
    def get_user_id(session: Session):
        """Returns current session user id."""
        if session == ServerSessionFlag:
            return None
        else:
            return session.get('user_id')

    def has_permission(self, session: Session, permission: str):
        """Checks if a user session has a particular permission."""
        if session == ServerSessionFlag:
            return True
        else:
            return permission in session['permissions'] or self.system_user(session)

    @staticmethod
    def system_user(session: Session):
        """Checks if user session has the system permission."""
        if session == ServerSessionFlag:
            return True
        else:
            return PermissionKeys.GLOBAL_SYSTEM_PERMISSION in session['permissions']

    def _compile_validators(self) -> dict:
        validators = {}
        for method_name, schema in self.validators.items():
            validator_order = self._compile_schema(schema)
            validators[method_name] = tuple(validator_order)
        return validators

    @staticmethod
    def _compile_schema(validator) -> tuple:
        validator_func, validator_schema, validator_call_before = None, None, None
        if isinstance(validator, dict):
            validator_schema = validator.get('schema')
            validator_func = validator.get('func')
            validator_call_before = validator.get('call_before_schema')
        elif callable(validator):
            validator_func = validator
        else:
            validator_schema = validator

        validator_order = []

        if validator_schema:
            validator_schema = compile_schema(validator_schema)
            validator_order.append(validator_schema)

        if validator_func:
            if validator_call_before:
                validator_order.insert(0, validator_func)
            else:
                validator_order.append(validator_func)

        return tuple(validator_order)


class AbstractRPCTransportInterface(abc.ABC):
    """
    This interfaces describes methods of a transport to be able to be used by
    the :class:`.AbstractRPCClientService`.
    """

    @abc.abstractmethod
    async def rpc_request(
            self, uri: str,
            request: Union[jsonrpc.RPCRequest, List[jsonrpc.RPCRequest]],
            headers: Optional[Dict[str, Any]]) -> Union[dict, list]:
        """
        This method depends on a specific transport.

        :param uri: RPC endpoint, queue name etc.
        :param request: request body (JSON compatible)
        :param headers: optional request headers
        """


class AbstractTokenInterface(abc.ABC):
    """
    This interface describes a token provider service methods to be able to be
    used by the :class:`.AbstractRPCClientService`.
    """

    @abc.abstractmethod
    async def get_token(self) -> str:
        """Must always return a valid auth token."""
