"""
Tools for python logging.

Usage
-----

You can create a loggable class and use its personal logger (configurable).

.. code-block:: python

    from kaiju_tools.logging import Loggable

    class MyClass(Loggable):

        def __init__(self, a, b, logger=None):
            Loggable.__init__(self, logger)

    obj = MyClass(1, 2)
    obj.logger.info('Wow! Im loggin')  # will use 'MyClass' logger


To customize logging name you must rewrite `_get_logger_name` method. By
default it sets the logger name to the name of a class. You can customize it
for instance-wise behaviour for example.

.. code-block:: python

    from kaiju_tools.logging import Loggable

    class MyClass(Loggable):

        def __init__(self, *args, logger=None, **kws):
            Loggable.__init__(self, logger)

        def _get_logger_name(self):
            return f'{super().get_logger_name()}.{id(self)}'


You may pass another logger instance on init, so the class's logger will
automatically become a child of this logger (useful when your class is a part
of another class / app / test suite). By default all loggers are inherited
directly from the root logger.

.. code-block:: python

    import logging
    from kaiju_tools.logging import Loggable

    class MyClass(Loggable):
        pass

    app_logger = logging.getLogger("app")
    obj = MyClass(logger=app_logger)
    obj.logger.info('Cool!')  # will use 'app.MyClass' logger by default


Classes
-------

"""

import abc
import logging
import logging.config
import sys
from functools import partial

__all__ = ('Loggable', 'get_logger_settings')


class Loggable(abc.ABC):
    """Allows a class to have its own logger.

    :param logger: parent logger or None for root as parent
    """

    def __init__(self, logger: logging.Logger = None):
        self._logger = self._get_logger(logger)

    @property
    def logger(self) -> logging.Logger:
        """Instance logger. By default logger name equals to the class's name."""

        return self._logger

    def _get_logger(self, logger):
        if logger:
            logger = logger.getChild(self._get_logger_name())
        else:
            logger = logging.getLogger(self._get_logger_name())
        return logger

    def _get_logger_name(self):
        return self.__class__.__name__


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class LogFormatter(logging.Formatter):

    colors = {
        logging.DEBUG: Colors.GRAY,
        logging.INFO: Colors.RESET,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.RED
    }

    def format(self, record):
        msg = super().format(record)
        color = self.colors[record.levelno]
        return f'{color}{msg}{Colors.RESET}'


class LogFormatterNoStackTrace(LogFormatter):

    def format(self, record) -> str:
        if record.exc_info:
            t, exc, trace = record.exc_info
            record.msg = f'{record.msg} / [{t.__name__}] {exc}'
            record.exc_info = None
        return super().format(record)


def get_logger_settings(level: str, debug: bool):
    """Default set of usefull logger settings."""

    logger = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            "trace": {
                '()': LogFormatter,
                'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
                "datefmt": '%Y-%m-%d %H:%M:%S',
            },
            "no_trace": {
                '()': LogFormatterNoStackTrace,
                'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
                "datefmt": '%Y-%m-%d %H:%M:%S'
            }
        },
        "handlers": {
            "console": {
                "class": 'logging.StreamHandler',
                "formatter": 'default',
                "level": level,
                'stream': sys.stdout
            },
        },
        'loggers': {
            'app': {
                'handlers': ['console'],
                'level': level,
                'propagate': True
            }
        }
    }

    if debug:
        logger['handlers']['console']['formatter'] = 'trace'
    else:
        logger['handlers']['console']['formatter'] = 'no_trace'

    return logger


def init_logger(settings):

    logger_settings = get_logger_settings(settings.main['loglevel'], settings.app.debug)
    logging.config.dictConfig(logger_settings)
    logger = logging.getLogger('app')

    # TODO: make it more obvious to configure
    if settings.etc.sentry['enabled']:

        # raven install is required for Sentry
        from raven import Client
        from raven.handlers.logging import SentryHandler
        from raven_aiohttp import QueuedAioHttpTransport

        client = Client(
            dsn=settings.etc.sentry['dsn'],
            site='elemento.systems',
            name=settings.main.name,
            environment=settings.main.env,
            sample_rate=settings.etc.sentry['sample_rate'],
            traces_sample_rate=settings.etc.sentry['traces_sample_rate'],
            auto_log_stacks=True,
            transport=partial(QueuedAioHttpTransport, workers=1))
        handler = SentryHandler(client)
        handler.setLevel('ERROR')
        logger.addHandler(handler)

    return logger
