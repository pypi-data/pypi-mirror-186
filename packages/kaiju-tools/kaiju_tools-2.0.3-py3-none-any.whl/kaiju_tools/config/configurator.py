import abc
import pathlib
import uuid
from functools import partial
from typing import Union

import yaml

from ..serialization import Serializable, load
from ..logging import Loggable
from ..mapping import recursive_update
from ..templates import Template

__all__ = (
    'Configurator', 'Config', 'ConfigurationError',
    'BaseSettings', 'RunSettings', 'CustomSettings',
    'MainSettings', 'WebAppSettings', 'ConfigSettings'
)


class ConfigurationError(KeyError):
    pass


class BaseSettings(abc.ABC):

    def __getitem__(self, item):
        return self.__dict__[item]

    def __getattr__(self, item):
        return self[item]


class CustomSettings(Serializable, BaseSettings):
    """
    Arbitrary settings (etc).
    """

    __slots__ = ('kws',)

    def __init__(self, **kws):
        self.kws = kws

    def repr(self) -> dict:
        return self.kws


class MainSettings(Serializable, BaseSettings):
    """
    Main app settings passed to the application mapping.
    """

    DEFAULT_LOG_LEVEL = 'INFO'

    __slots__ = ('name', 'version', 'env', 'id', 'loglevel')

    def __init__(
        self, name: str, version: str, env: str, id: Union[uuid.UUID, str] = None,
        loglevel: str = DEFAULT_LOG_LEVEL
    ):
        """
        :param name: app (project) name
        :param version: app version
        :param env: run environment
        :param id: unique app instance UUID
        :param loglevel: root logger log level
        """
        self.id = str(uuid.UUID(str(id))) if id else str(uuid.uuid4())
        self.name = str(name).lower() if name else 'app'
        self.version = str(version).lower()
        self.env = str(env).lower() if env else 'dev'
        self.loglevel = str(loglevel.upper())


class WebAppSettings(Serializable, BaseSettings):
    """
    Settings for an aiohttp Application() object.
    """

    __slots__ = ('kws',)

    def __init__(self, **kws):
        self.kws = kws

    def repr(self) -> dict:
        return self.kws


class RunSettings(Serializable, BaseSettings):
    """
    Settings for aiohttp run_app() callable.
    """

    __slots__ = ('host', 'port', 'path', 'shutdown_timeout')

    def __init__(
            self, host: str = None, port: int = None, path: str = None,
            shutdown_timeout: float = 60.
    ):
        self.host = str(host) if host else None
        self.port = int(port) if port else None
        self.path = str(path) if path else None
        self.shutdown_timeout = float(shutdown_timeout)


class ConfigSettings(Serializable):
    """
    Settings block.
    """

    __slots__ = ('app', 'run', 'main', 'services', 'etc')

    def __init__(
            self, app: dict = None, run: dict = None, main: dict = None,
            etc: dict = None, services: list = None
    ):
        """
        :param app: Application() object settings
        :param run: run_app() callable settings
        :param main: main app settings passed to the Application() mapping
        :param etc: other settings
        :param services: ServiceContextManager() settings for app services
        """

        if app is None:
            app = {}
        self.app = WebAppSettings(**app)

        if run is None:
            run = {}
        self.run = RunSettings(**run)

        if main is None:
            main = {}
        self.main = MainSettings(**main)

        if etc is None:
            etc = {}
        self.etc = CustomSettings(**etc)

        if services is None:
            services = []
        self.services = services


class Config(Serializable, BaseSettings):
    """
    Configuration file.
    """

    __slots__ = ('settings', 'tags', 'version')

    def __init__(self, settings: dict = None, tags: list = None, version: str = None):
        """
        :param settings: application settings
        :param tags: config file tags
        :param version: config file format version
        """
        if settings is None:
            settings = {}
        self.settings = ConfigSettings(**settings)
        self.tags = tuple(str(tag) for tag in tags) if tags else tuple()
        self.version = str(version) if version else None


class Configurator(Loggable):
    """
    The configurator class manages app configs and dependencies before the app start.
    """

    config_class = Config

    file_loaders = {
        '.json': load,
        '.yml': partial(yaml.load, Loader=yaml.SafeLoader),
        '.yaml': partial(yaml.load, Loader=yaml.SafeLoader),
    }

    def __init__(self, env: dict = None, logger=None):
        """
        :param env: custom environment variables mapping (updated by `os.environ`)
        :param logger:
        """
        super().__init__(logger=logger)
        self._env = env if env else {}

    def from_dict(self, data: dict) -> config_class:
        data = Template(data).fill(self._env)
        config = self.config_class(**data)
        return config

    def from_file(self, path: str, base_path: str = None) -> config_class:
        if base_path and base_path != path:
            config = self._from_file(base_path)
            updated = self._from_file(path)
            config = recursive_update(config, updated)
        else:
            config = self._from_file(path)
        return self.from_dict(config)

    def _from_file(self, path) -> dict:
        path = pathlib.Path(path)
        if not path.exists() or path.is_dir():
            raise ValueError(
                'Config path doesn\'t exist or it\'s a directory.'
                ' "%s" - not found!' % path)

        loader = self.file_loaders.get(path.suffix)
        if not loader:
            raise ValueError('Unknown config file extension %s.' % path.suffix)
        data = self._load_data_from_file(path, loader)
        return data

    @staticmethod
    def _load_data_from_file(path, loader: callable) -> dict:
        with open(path) as f:
            data = loader(f)
        return data
