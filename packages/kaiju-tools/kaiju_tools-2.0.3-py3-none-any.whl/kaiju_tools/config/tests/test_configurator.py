import os

from ..configurator import Configurator


def test_settings(logger):

    test_config = {
        'version': '1.0',
        'settings': {
            'main': {
                'name': '[APP_NAME]',
                'version': '0.0',
                'env': 'dev',
                'loglevel': 'DEBUG'
            },
            'app': {
            },
            'run': {
                'host': 'localhost',
                'port': 8080
            },
            'services': [
                {
                    'cls': 'JSONRPCServer',
                    'info': 'some server',
                    'settings': {}
                }
            ]
        }
    }

    custom_env = {
        'APP_NAME': 'custom_app'
    }

    configurator = Configurator(env=custom_env, logger=logger)
    config = configurator.from_dict(test_config)

    logger.debug(config)

    assert config.settings.main.name == 'custom_app'

