import asyncio

import uuid
from typing import *

import pytest

from  ..abc import AbstractRPCCompatible
from ..services import JSONRPCServer
from ...services import Service

from ... import jsonschema as j
from ...exceptions import ValidationError


@pytest.fixture
def rpc_interface(logger):
    return JSONRPCServer(
            app=None, max_parallel_tasks=5, deadline_check_interval=0.05,
            request_queue_size=2, debug=True, logger=logger)


@pytest.fixture
def rpc_compatible_service():

    class TestService(Service, AbstractRPCCompatible):

        service_name = 'm'

        @property
        def validators(self) -> dict:
            return {
                'validated': j.Object({
                    'a': j.Integer(),
                    'b': j.Integer()
                }),
                'validated_2': self._custom_validator
            }

        @property
        def permissions(self) -> Optional[dict]:
            return {
                '*': 'guest'
            }

        @property
        def routes(self) -> dict:
            return {
                'echo': self.echo,
                'aecho': self.async_echo,
                'sum': self.sum,
                'fail': self.failed,
                'long_echo': self.async_long_echo,
                'split': self.split,
                'standard_echo': self.async_standard_echo,
                'validated': self.validated_method,
                'validated_2': self.validated_method
            }

        def sum(self, x: float, y: float) -> float:
            """A sum command.

            :param x: first value
            :example x: 7
            :param y: second value
            :example y: 6
            :returns: sum of two values
            """

            return x + y

        def split(self, value: str, delimiter: str) -> List[str]:
            """Splits a string value by delimiter.

            :returns: split parts
            """

            return value.split(delimiter)

        async def failed(self):
            """A simple wrong command."""

            raise ValueError('Something bad happened.')

        def echo(self, *args, **kws):
            """A simple echo command which accepts any arguments."""

            self.logger.info('Executing echo.')
            return args, kws

        async def async_echo(self, *args, **kws):
            """A simple echo command which accepts any arguments."""

            self.logger.info('Executing async echo.')
            await asyncio.sleep(0.01)
            return args, kws

        async def async_standard_echo(self, *args, **kws):
            """A simple echo command which accepts any arguments."""

            self.logger.info('Executing long echo.')
            await asyncio.sleep(0.5)
            return args, kws

        async def async_long_echo(self, *args, **kws):
            """A simple echo command which accepts any arguments."""

            self.logger.info('Executing long echo.')
            await asyncio.sleep(3)
            return args, kws

        def validated_method(self, a: int, b: int):
            """A method with a validated input."""

            return a * b

        def _custom_validator(self, data: dict):
            if type(data.get('a')) is not int or type(data.get('b')) is not int:
                raise ValidationError('Values must be INT.')

    return TestService


@pytest.fixture
def user_session():
    return {
        'user_id': uuid.uuid4(),
        'permissions': [
            AbstractRPCCompatible.PermissionKeys.GLOBAL_USER_PERMISSION
        ]
    }


@pytest.fixture
def admin_session():
    return {
        'user_id': uuid.uuid4(),
        'permissions': [
            AbstractRPCCompatible.PermissionKeys.GLOBAL_SYSTEM_PERMISSION
        ]
    }


@pytest.fixture
def guest_session():
    return {
        'user_id': uuid.uuid4(),
        'permissions': [
            AbstractRPCCompatible.PermissionKeys.GLOBAL_GUEST_PERMISSION
        ]
    }
