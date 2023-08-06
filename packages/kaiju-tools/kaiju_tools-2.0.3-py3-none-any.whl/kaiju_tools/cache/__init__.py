"""
Shared cache services.

How to use
----------

There are a bunch of default methods for work with caches (see `CacheServiceInterface`).

.. code-block:: python

    await cache.set('key', {'value': True}, ttl=100)
    if await cache.exists('key'):
        await cache.get('key')

`get` `set` `exists` `delete`       - for single key operations
`mget` `mset` `mexists` `mdelete`   - for multiple keys operations

You may want to use a lazy set/delete operations (i.e. performed in background)
to speed up your functions a little more.

.. code-block:: python

    await cache.set('key', {'value': True}, ttl=100, nowait=True)

In this case there's a potential risk to fail (although all background operations
are wrapped in a retry function) but you don't need to wait for the send-return.

Usage in your project
---------------------

It is expected to be use with a service initialization system, but you can
use it directly if you provide an aiohttp app instance and will call init/close
manually (if required).

Tests
-----

The tests use **Docker** to set up a Redis or other environment, i.e. you need
to install the docker engine to be able to actually test.

Implementation
--------------

It consists of a base class implementing the skeleton of the methods and specific
backend-oriented classes.

.. uml::

    @startuml

    CacheServiceInterface <|-- BaseCacheeService <|-- RedisCacheService

    @enduml

The class uses a simple namespace system, it prepends a namespace prefix and
a cache prefix before each key.

Thus the format is:

    '<namespace>:<cache_prefix>:<key>' = '<value>'

So a key would look like this:

    'app:cache:my_key_42' = '123'

Package structure
-----------------

- abc - base classes
- etc - other data (status codes, shared constants, ...)
- tests - unit tests (pytest)
- services - list of implemented not abstract services

Implementing your own backend
-----------------------------

Inherit from `BaseCacheService` and implement all the abstract async methods
for your backend. They should raise a proper error classes in specific cases
(read the methods description!). You also may want to change `__init__` a bit
for a proper type hinting for your transport. See how `RedisCacheService`
(in kaiju-redis repository) does it.

Add your backend into `.tests.test_cache` for testing
(again, see `test_redis_cache_service` (in kaiju-redis repository) for example).
You will need to provide own container and transport fixtures
(or import them from an other kaiju package).
"""

from .abc import *
from .local_cache import *
from .services import *
