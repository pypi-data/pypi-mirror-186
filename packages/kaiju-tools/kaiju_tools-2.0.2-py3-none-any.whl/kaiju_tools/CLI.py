"""
CLI services and registries.
"""

import abc
import errno
import traceback
from argparse import ArgumentParser

from aiohttp.web import Application, AppRunner

from .class_registry import AbstractClassRegistry
from .services import ContextableService
from .rpc.abc import AbstractRPCCompatible

from .loop import loop

__all__ = [
    'run_command', 'Commands', 'CLIService', 'AbstractCommand'
]


class AbstractCommand(ContextableService, abc.ABC):

    service_name = None  #: required command name
    run_app = True

    def __init__(self, app: Application, logger=None):
        super().__init__(app=app, logger=logger)
        self._runner = AppRunner(app)
        self._closed = True

    @classmethod
    def get_parser(cls) -> ArgumentParser:
        """Custom argument parser."""

        return ArgumentParser()

    @abc.abstractmethod
    async def command(self, **kws):
        """Custom command."""

    async def init(self):
        """Custom init"""

    async def close(self):
        """Custom cleanup."""

    @property
    def closed(self) -> bool:
        return self._closed

    def run(self):
        result = 1
        try:
            self.logger.info('Setting up a webapp runner.')
            if self.run_app:
                loop.run_until_complete(self._runner.setup())
            self.logger.info('Initialization.')
            loop.run_until_complete(self.init())
            self._closed = False
            params, _ = self.get_parser().parse_known_args()
            self.logger.info(
                'Executing command "%s" with params: "%s"',
                self.service_name, params)
            result = loop.run_until_complete(self.command(**params.__dict__))
        except Exception as err:
            self.logger.error('Command failed.', exc_info=err)
        finally:
            self.logger.info('Closing.')
            loop.run_until_complete(self.close())
            if self.run_app:
                loop.run_until_complete(self._runner.cleanup())
            loop.close()
            self._closed = True
            return result


class Commands(AbstractClassRegistry):
    """Map of all available commands. User MUST register it in this class."""

    base_classes = (AbstractCommand,)

    @staticmethod
    def class_key(obj) -> str:
        return obj.service_name


commands = Commands()


def run_command(app: Application, command: str, commands_registry=commands) -> int:
    if command in commands_registry:
        cmd = commands_registry[command]
        cmd = cmd(app=app, logger=app.logger.getChild('CLI'))
        result = cmd.run()
    else:
        app.logger.error('Unknown command "%s".', command)
        result = errno.ENOENT
    return result


class CLIService(ContextableService, AbstractRPCCompatible):
    """CLI to RPC adapter Use it to execute CLI commands via RPC."""

    service_name = 'CLI'

    def __init__(self, app, logger=None):
        super().__init__(app=app, logger=logger)
        self._routes = {}
        for cmd_name in commands:
            cmd_cls = commands[cmd_name]
            cmd = cmd_cls(app=app, logger=logger)
            self._routes[cmd_name] = self._wrapper(cmd)

    @staticmethod
    def _wrapper(cmd):

        async def _wrap(**kws):
            async with cmd:
                return await cmd.command(**kws)

        return _wrap

    @property
    def routes(self) -> dict:
        return self._routes
