"""
Web app initialization scripts.
"""

import logging
import os
import sys

from aiohttp.web import Application, run_app

import kaiju_tools.loop  # do not remove
from kaiju_tools.CLI import run_command
from kaiju_tools.config import ConfigLoader, Config, ConfigSettings
from kaiju_tools.services import service_class_registry, ServiceContextManager, App
from kaiju_tools.logging import init_logger
from kaiju_tools.http.exceptions import error_middleware

__all__ = (
    'App', 'init_config', 'init_app', 'main'
)


def init_config() -> (str, Config):
    debug = bool(ConfigLoader._init_env_value(os.getenv('DEBUG'))) | ('--debug' in sys.argv)
    level = 'DEBUG' if debug else 'INFO'
    logging.basicConfig(level=level)
    config_loader = ConfigLoader(
        base_config_path='./settings/config.yml',
        base_env_path='./settings/env.json',
        default_env_path='./settings/env.local.json',
        default_config_path='./settings/config.yml',
        logger=logging.root
    )
    command, config = config_loader.configure()
    logging.root.handlers = []
    return command, config


def init_app(settings: ConfigSettings, attrs: dict = None) -> App:
    logger = init_logger(settings)
    app: App = Application(middlewares=[error_middleware], logger=logger, **settings.app)

    for key, value in settings.main.repr().items():
        app[key] = value
        setattr(app, key, value)

    if attrs:
        for key, value in attrs.items():
            app[key] = value
            setattr(app, key, value)

    app.settings = settings
    app.services = services = ServiceContextManager(
        app=app, settings=settings.services,
        class_registry=service_class_registry,
        logger=app.logger
    )
    app.cleanup_ctx.extend(services)

    return app


def main(_init_app):
    command, config = init_config()
    settings: ConfigSettings = config.settings
    app: App = _init_app(settings)
    if settings.app.debug:
        print('\n-- RUNNING IN DEBUG MODE --\n')
    if command:
        run_command(app, command)
    else:
        run_app(app, **settings.run)
