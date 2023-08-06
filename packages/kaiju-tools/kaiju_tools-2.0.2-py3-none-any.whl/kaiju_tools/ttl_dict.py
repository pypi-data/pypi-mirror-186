"""
A simple mutable mapping that supports TTL.

It can be used for arbitrary data caching. TTL value is global for all the
objects. If you need more complex TTL behaviour, use specialized cache solutions
like Redis.

Basic use is the same as for a dictionary object.

.. code-block:: python

    cache = TTLDict({'sht': 666})
    assert 'sht' in cache
    assert cache['sht'] == 666
    del d['sht']

Objects surpassed their TTL are stored until some action is performed
(like counting length, accessing keys or values, etc.)

.. code-block:: python

    cache = TTLDict({'sht': 666})
    cache.set_ttl(1)
    sleep(3)

    # 'sht' is still in the cache but if you try to access it, it will be pruned
    # you can directly call refresh to free some memory manually

    cache.refresh()


Performance
-----------

Here is performance data for different operations and different number of keys.
Number of operations per second and relative performance compared to a normal `dict`.

.. code-block::

    2020-01-24
    Intel(R) Core(TM) i5-7360U CPU @ 2.30GHz
    Testing TTL dict performance (3000 cycles, 3 runs)...

GET:
  10    1524277 sec^-1 | 15.0%
 100     727588 sec^-1 | 6.8%
1000     132112 sec^-1 | 1.4%

SET:
  10     579831 sec^-1 | 12.0%
 100     317694 sec^-1 | 6.8%
1000     193648 sec^-1 | 4.5%

LENGTH:
  10    1413810 sec^-1 | 18.0%
 100    1254652 sec^-1 | 16.6%
1000    1177403 sec^-1 | 17.0%


Classes
-------

"""

import bisect
import sys
from collections.abc import MutableMapping
from time import time

__all__ = ['TTLDict']


class TTLDict(MutableMapping):
    """A simple TTL dict mostly compatible with a normal one."""

    TTL = 60  #: default TTL in ms
    __slots__ = ('_ttl', '_dict', '_ttls', '_keys')

    def __init__(self, *args, **kws):
        self._ttl = int(self.TTL)
        self._dict = dict()  # here key: (value, index) data will be stored
        self._keys = []  # sorted list of keys
        self._ttls = []  # sorted list of deadlines
        for key, value in dict(*args, **kws).items():
            self[key] = value

    def __getitem__(self, key):
        value = self._dict[key]
        n = self._keys.index(key)
        t = self._ttls[n]
        if t > time():
            return value
        else:
            del self[key]
            raise KeyError(key)

    def __setitem__(self, key, value):
        return self.set(key, value, self._ttl)

    def __delitem__(self, key):
        n = self._keys.index(key)
        del self._keys[n]
        del self._ttls[n]
        del self._dict[key]

    def __len__(self):
        self.refresh()
        return len(self._dict)

    def __bool__(self):
        return bool(len(self))

    def __contains__(self, item):
        return self.get(item) is not None

    def __eq__(self, other):
        self.refresh()
        other.refresh()
        assert other._dict == self._dict

    def __iter__(self):
        return iter(self.keys())

    def get(self, item, default=None):
        """Similar to `dict().get`."""
        try:
            return self[item]
        except KeyError:
            return default

    def set(self, key, value, ttl: int):
        """
        Similar to `__setitem__` but you may specify per-key ttl.
        """
        if key in self._dict:
            del self[key]
            self.set(key, value, ttl)
        else:
            if ttl:
                t = int(time() + ttl)
            else:
                t = float('Inf')
            n = bisect.bisect_left(self._ttls, t)
            self._ttls.insert(n, t)
            self._keys.insert(n, key)
            self._dict[key] = value

    def values(self):
        """Similar to `dict().values`."""
        self.refresh()
        return self._dict.values()

    def keys(self):
        """Similar to `dict().keys`."""
        self.refresh()
        return self._dict.keys()

    def items(self):
        """Similar to `dict().items`."""
        return zip(self._dict.keys(), self.values())

    def set_ttl(self, ttl: int):
        """
        Set default ttl to a new value

        :param ttl: TTL value in seconds
        """
        if not ttl:
            ttl = sys.maxsize
        elif ttl < 0:
            raise ValueError('TTL value must be greater than zero.')
        ttl = int(ttl)
        self._ttl = ttl

    def refresh(self):
        """Removes old records.

        .. note::

            This method is called each time one calls a `TTLDict.__len__`
            or any other method that must provide an actual dictionary state.

        """
        t = int(time())
        n = bisect.bisect_right(self._ttls, t)
        if n:
            self._ttls = self._ttls[n:]
            keys, self._keys = self._keys[:n], self._keys[n:]
            for key in keys:
                del self._dict[key]
