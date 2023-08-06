"""
App setting management.

Application config consists of multiple sections.

.. code-block:: json

    {
        "version": "1.0",       // optional config version
        "tags": [],             // optional list of tags
        "requirements": [],     // list of additional requirements installed on start
        "settings": {
            "app": {},          // aiohttp app specific settings
            "run": {},          // aiohttp run_app settings (host, port, socket etc.)
            "main": {},         // main settings (name, identifier and other)
            "etc": {},          // other settings
            "services": [],     // service settings
        }  // app settings
    }

There are several ways to define config parameters. The most simple is to write
a value directly in a config file.

See :class:`.Config` for more info about configuration.

"""

from .configurator import *
from .config_loader import *
