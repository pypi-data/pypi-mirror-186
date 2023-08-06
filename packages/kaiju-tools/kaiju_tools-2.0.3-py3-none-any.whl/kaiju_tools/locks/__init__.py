"""
A service class to manage locks between multiple apps via a shared storage.

How to use
----------

There are two options: to acquire a lock and to release it.

.. code-block:: python

    await locks.acquire('some_lock', 'my_service')
    await locks.release('some_lock', 'my_service')

A service name must match otherwise it will throw a `LockError` because a lock
can be released only by its owner.

The lock service automatically sets lock TTLs to a small value (couple of minutes)
and renews it periodically. It should prevent locks from hanging if an app
quits unexpectedly.

Usage in your project
---------------------

It is expected to be use with a service initialization system, but you can
use it directly if you provide an aiohttp app instance and will call init/close
manually.

Tests
-----

The tests use **Docker** to set up a Redis or other environment, i.e. you need
to install the docker engine to be able to actually test.

Implementation
--------------

It consists of a base class implementing the skeleton of the methods and specific
backend-oriented classes.

The class stores all true TTLs locally and creates a keys with short lifetimes
(~1min) which should prevent from locking when app unexpectedly exits. Each
key stores its owner identifier so only the owner can release the key (obviously
you can omit this behaviour by specifying the same owner id for all the locks).

Package structure
-----------------

- abc - base classes
- etc - other data (status codes, shared constants, ...)
- exceptions - exception classes used specifically by the locks service
- tests - tests for lock services

Implementing your own backend
-----------------------------

Inherit from `BaseLocksService` and implement all the abstract async methods
for your backend. They should raise a proper error classes in specific cases
(read the methods description!). You also may want to change `__init__` a bit
for a proper type hinting for your transport. See how `RedisLocksService`
(in kaiju-redis repository) does it.

Add your backend into `.tests.test_locks` for testing
(again, see `test_redis_locks_service` (in kaiju-redis repository) for example).
You will need to provide own container and transport fixtures
(or import them from an other kaiju package).
"""

from .etc import *
from .exceptions import *
from .abc import *
