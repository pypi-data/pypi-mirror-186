"""
Contains serialization tools and classes, incl. json `dumps` and `loads` with
default best-fit settings, hashable and serializable abstract classes.

Usage
-----

If you want only serialization capabilities, then you should define a subclass
of `Serializable`. It provides default algorithms for representation,
json serializing and loading.

.. code-block:: python

    from kaiju_tools.serialization import Serializable

    class MyClass(Serializable):

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self._c = a + b  # underscored attr won't be serialized

    obj = MyClass(1, 2)
    obj.repr()  # will return {'a': 1, 'b': 2}
    s = obj.to_json()  # same but as json string
    MyClass.from_json(s)  # will create an instance of `MyClass` from given json string


To customize serialization you may set `serializable_attrs` or implement
`repr` method by yourself. The only thing you should watch for is that the
`repr` attribute keys are compatible with the class's `__init__` method.

.. code-block:: python

    from kaiju_tools.serialization import Serializable

    class MyClass(Serializable):
        serializable_attrs = {'a', 'b'}

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.c = a + b  # won't be serialized because it's not in the serializable_attrs


    class MyOtherClass(Serializable):

        def __init__(self, a, b):
            self.items = [a, b]

        def repr(self):
            return {'a': self.items[0], 'b': self.items[1]}


`Comparable` class implements `__eq__` as well. It compares `repr` keys one by
one.

.. code-block:: python

    from kaiju_tools.serialization import Comparable

    class MyClass(Comparable):

        def __init__(self, a, b):
            self.a = a
            self.b = b

    obj1 = MyClass(1, 2)
    obj2 = MyClass(1, 3)
    assert obj1 != obj2


`Hashable` class implements both `__eq__` and `__hash__` methods so you
can use instances of the class as dictionary keys.
It also implements `uuid` property based on *md5* hash value of an object's
attributes, thus you can use it for duplicate checks for objects in the database
or for unique content-based ID generation.

.. code-block:: python

    from kaiju_tools.serialization import Hashable

    class MyClass(Hashable):

        def __init__(self, a, b):
            self.a = a
            self.b = b

    obj1 = MyClass(1, 1)
    _map = {obj1: True}
    obj2 = MyClass(1, 1)
    assert obj2 in _map
    assert obj1.uuid == obj2.uuid


Classes
-------

"""

import abc
import uuid
from collections.abc import Mapping
from hashlib import md5

from .encoding.json import dumps, loads, load, dumps_bytes

__all__ = (
    'dumps', 'dumps_bytes', 'loads', 'load', 'uuid_hash',
    'Serializable', 'Comparable', 'Hashable'
)


class Serializable(Mapping, abc.ABC):
    """
    This means that an object can be serialized / deserialized to and from
    JSON or a repr string.

    Because it's a subclass of `Mapping` class, it can be converted into `dict`
    object using `dict()`.
    """

    serializable_attrs = None  #: Should be a frozenset or None. If None, then all will be used for serialization.
    include_null_values = True  #: include null values in a representation

    def __iter__(self):
        return iter(self.repr())

    def __getitem__(self, item):
        return self.repr()[item]

    def __len__(self):
        return len(self.repr())

    def repr(self) -> dict:
        """Must return a representation of object __init__ arguments.

        By default it will ignore all underscore elements.
        """

        _repr = {}

        if self.serializable_attrs is None:
            if self.__slots__:
                for slot in self.__slots__:
                    if not slot.startswith('_') and hasattr(self, slot):
                        v = getattr(self, slot)
                        if not self.include_null_values and v is None:
                            continue
                        if isinstance(v, Serializable):
                            _repr[slot] = v.repr()
                        else:
                            _repr[slot] = v
            else:
                for k, v in self.__dict__.items():
                    if not self.include_null_values and v is None:
                        continue
                    if not k.startswith('_'):
                        if isinstance(v, Serializable):
                            _repr[k] = v.repr()
                        else:
                            _repr[k] = v
        else:
            if self.__slots__:
                for slot in self.__slots__:
                    if slot in self.serializable_attrs and hasattr(self, slot):
                        v = getattr(self, slot)
                        if not self.include_null_values and v is None:
                            continue
                        if isinstance(v, Serializable):
                            _repr[slot] = v.repr()
                        else:
                            _repr[slot] = v
            else:
                for k, v in self.__dict__.items():
                    if not self.include_null_values and v is None:
                        continue
                    if k in self.serializable_attrs:
                        if isinstance(v, Serializable):
                            _repr[k] = v.repr()
                        else:
                            _repr[k] = v

        return _repr

    def __repr__(self):
        return f'{self.__class__.__name__}(**{self.repr()})'

    def to_json(self, *args, **kws) -> str:
        """This method is equivalent to `dumps(obj)`."""

        return dumps(self.repr(), *args, **kws)

    @classmethod
    def from_json(cls, s: str, *args, **kws):
        """You can use this to construct a new object of the class from json."""

        return cls(**loads(s, *args, **kws))


class Comparable(Serializable, abc.ABC):
    """
    Same as `Serializable`, but also implements comparison operation.

    Two objects are considered equal if their representation dictionaries are
    equal and both objects are of the same class.
    """

    def __eq__(self, other):
        if type(self) == type(other):
            r1, r2 = self.repr(), other.repr()
            for k, v in r1.items():
                if r2.pop(k, None) != v:
                    return False
            for k, v in r2.items():
                if r1.pop(k, None) != v:
                    return False
            return True
        return False


class Hashable(Comparable, abc.ABC):
    """
    Same as `Comparable` but also implements hashing.
    """

    def __hash__(self):
        return hash(dumps(self._hash(), sort_keys=True))

    @property
    def uuid(self) -> uuid.UUID:
        """Hash representation as UUID. You may use it in database as primary
        key to protect your data from duplicates."""

        s = dumps(self._hash(), sort_keys=True)
        return uuid.UUID(md5(s.encode()).hexdigest())

    def _hash(self) -> dict:
        return self.repr()


def uuid_hash(value) -> uuid.UUID:
    """
    MD5 hash of an arbitrary value.

    :param value: should be a string or JSON serializable object
    :returns: MD5 hash in the form of UUID
    """

    if not type(value) is str:
        value = dumps(value, sort_keys=True)
    _hash = uuid.UUID(md5(value.encode()).hexdigest())
    return _hash
