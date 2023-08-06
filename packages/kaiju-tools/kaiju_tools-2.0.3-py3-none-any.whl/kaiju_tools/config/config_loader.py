"""
Config loader class is intended to be used before everything to provide an initial
config for the app and app runners.

Currently *JSON* and *YAML* formats are supported for config files.
"""

import logging
import os
import pathlib
import subprocess
import uuid
from ast import literal_eval
from argparse import ArgumentParser

from ..serialization import load
from ..services import service_class_registry
from ..logging import Loggable
from .configurator import Configurator, Config, ConfigurationError

__all__ = ('ConfigLoader', 'get_cli_parser')


def get_cli_parser() -> ArgumentParser:
    """
    Argument parser with some predefined useful parameters.
    """

    _parser = ArgumentParser(
        prog='aiohttp web application',
        description='web application run settings'
    )
    _parser.add_argument(
        '--host', dest='host', default=None,
        help='web app host (default - from settings)'
    )
    _parser.add_argument(
        '--port', dest='port', type=int, default=None,
        help='web app port (default - from settings)'
    )
    _parser.add_argument(
        '--path', dest='path', default=None, metavar='FILENAME',
        help='web app socket path (default - from settings)'
    )
    _parser.add_argument(
        '--id', dest='id', default=None,
        help='web app unique id (default - from settings)'
    )
    _parser.add_argument(
        '--debug', dest='debug', action='store_true', default=False,
        help='run in debug mode (default - from settings)'
    )
    _parser.add_argument(
        '--cfg', dest='cfg', default=None, metavar='FILENAME',
        help='yaml config path (default to ./settings/config.local.yaml, fallback to ./settings/config.yaml)'
    )
    _parser.add_argument(
        '--log', dest='loglevel', default=None,
        choices=tuple(logging._nameToLevel.keys()),
        help='log level'
    )
    _parser.add_argument(
        '--env-file', dest='env_file', default=None, metavar='FILENAME',
        help='env file path (default to ./settings/env.local.json)'
    )
    _parser.add_argument(
        '--base-env-file', dest='base_env_file', default=None, metavar='FILENAME',
        help='base/fallback env file path (default to ./settings/env.local.json)'
    )
    _parser.add_argument(
        '--env', dest='env', default=None, action='append', metavar='KEY=VALUE',
        help='overrides env variable (may be used multiple times)'
    )
    _parser.add_argument(
        '--no-os-env', dest='no_os_env', action='store_true', default=False,
        help='do not use OS environment variables'
    )
    _parser.add_argument(
        '--no-base-cfg', dest='no_base_cfg', action='store_true', default=False,
        help='do not use base config file'
    )
    _parser.add_argument(
        '--no-base-env', dest='no_base_env', action='store_true', default=False,
        help='do not use base env file'
    )
    _parser.add_argument(
        'cmd', metavar='COMMAND', default=None, nargs='?',
        help='optional management command to execute'
    )
    return _parser


class ConfigLoader(Loggable):
    """
    Config loader class. It is intended to be used before the app start.
    """

    DEFAULT_CONFIG_PATH = './config.yml'
    DEFAULT_ENV_PATH = './env.json'
    SERVICE_PACKAGE_PREFIX = 'kaiju'
    SERVICE_SUBMODULE_NAME = 'services'
    _pip_versions = ('pip3', 'pip')

    def __init__(
            self,
            base_config_path: str = DEFAULT_CONFIG_PATH,
            default_config_path: str = DEFAULT_CONFIG_PATH,
            base_env_path: str = DEFAULT_ENV_PATH,
            default_env_path: str = DEFAULT_ENV_PATH,
            service_package_prefix: str = SERVICE_PACKAGE_PREFIX,
            service_class_registry=service_class_registry,
            logger=None
    ):
        """
        :param base_config_path: used as a base template
        :param default_config_path: by default this file will be used for config
        :param base_env_path: base env file
        :param default_env_path: default environment file path
        :param service_class_registry: service class registry instance
        :param logger: arbitrary logger
        """
        super().__init__(logger=logger)
        self._base_env_path = base_env_path
        self._default_env_path = default_env_path
        self._default_config_path = default_config_path
        self._base_config_path = base_config_path
        self._service_package_prefix = service_package_prefix
        self.service_class_registry = service_class_registry

    def configure(self) -> (str, Config):
        """
        Full initial app configuration. Processes CLI and OS environment arguments
        and returns a run command name and a filled config object.

        This command should ideally be used before all the imports.
        """

        args = self._parse_cli_args()
        env = self._init_env(args)
        configurator = Configurator(env=env, logger=self.logger)
        config_path = args.get('cfg')
        if not config_path:
            config_path = self._default_config_path
        self.logger.debug('Loading config from "%s".', config_path)
        if args.get('no_base_cfg'):
            base_cfg = None
        else:
            base_cfg = self._base_config_path
        config = configurator.from_file(config_path, base_cfg)
        self._set_args_from_cli(args, config)
        command = args.get('cmd')
        self._register_service_classes_from_packages()
        return command, config

    def _init_env(self, args):
        env_path = args.get('env_file')

        def _load_env_file(filename) -> dict:
            if not filename:
                return {}
            filename = pathlib.Path(filename)
            if not filename.exists() or filename.is_dir():
                self.logger.warning(
                    'Env path doesn\'t exist. No env will be loaded.'
                    ' "%s" - not found!', env_path)
                return {}
            with open(str(filename)) as f:
                env = load(f)
            return env

        if args.get('no_base_env'):
            env = {}
        else:
            base_env_path = args.get('base_env_file')
            if not base_env_path:
                base_env_path = self._base_env_path
            if base_env_path:
                env = _load_env_file(self._base_env_path)
            else:
                env = {}

        if not env_path:
            env_path = self._default_env_path
        if env_path and env_path != self._base_env_path:
            env.update(_load_env_file(env_path))

        if not args.get('no_os_env'):
            env.update(self._get_os_env())

        if args.get('env'):
            env.update(args['env'])

        if args.get('debug'):
            env['app_debug'] = True
            env['main_loglevel'] = 'DEBUG'

        return env

    def _get_os_env(self):
        os_env = dict(os.environ)
        os_env = {k: self._init_env_value(v) for k, v in os_env.items()}
        if os_env.get('DEBUG'):
            os_env['app_debug'] = True
            os_env['main_loglevel'] = 'DEBUG'
        return os_env

    def _parse_cli_args(self) -> dict:
        parser = get_cli_parser()
        args = parser.parse_known_args()[0].__dict__
        env = args.get('env')
        if env:
            env_map = {}
            for record in env:
                k, v = record.split('=')
                env_map[k] = self._init_env_value(v)
            args['env'] = env_map
        return args

    @staticmethod
    def _set_args_from_cli(args: dict, config: Config):

        host = args.get('host')
        if host:
            config.settings.run.host = host

        port = args.get('port')
        if port:
            config.settings.run.port = port

        path = args.get('path')
        if path:
            config.settings.run.port = path

        id = args.get('id')
        if id:
            config.settings.main.id = str(uuid.UUID(id))

        debug = args.get('debug')
        if debug:
            config.settings.app.debug = debug

        log = args.get('loglevel')
        if log:
            config.settings.main.loglevel = log

    def _register_service_classes_from_packages(self):
        """
        Register service classes from packages in the registry.
        """
        self.logger.info('Registering services from packages.')
        packages = self._list_installed_packages(prefix=self._service_package_prefix)
        for package in packages:
            self._register_service_classes_from_package(package)

    def _list_installed_packages(self, prefix: str = None) -> list:
        cmd = ' || '.join(f'{pip} list --no-index' for pip in self._pip_versions)
        if prefix:
            grep = f"(grep -E -s '{prefix}' || :) | "
        else:
            grep = ''
        cmd = f"({cmd}) | {grep}awk '{{print $1}}'"
        self.logger.debug(cmd)
        result = subprocess.run(cmd, shell=True, check=False, capture_output=True)
        self.logger.debug(result)
        if result.returncode:
            raise ConfigurationError(result.stderr.decode())
        result = [
            package.replace('-', '_')
            for package in
            result.stdout.decode().strip().split('\n')
        ]
        return result

    def _register_service_classes_from_package(self, package_name: str):
        try:
            module = __import__(package_name + '.' + self.SERVICE_SUBMODULE_NAME)
        except ModuleNotFoundError:
            pass
        else:
            self.logger.debug('Registering services from "%s".', package_name)
            self.service_class_registry.register_classes_from_module(module)

    @staticmethod
    def _init_env_value(value: str):
        """Parse env arg from --env or unix environment."""

        if value is None:
            return None

        value = value.strip()

        if not value:
            return None

        _value = value.lower()
        if _value == 'true':
            value = True
        elif _value == 'false':
            value = False
        elif _value == 'none':
            value = None
        else:
            try:
                value = literal_eval(value)
            except Exception:
                pass
        return value
