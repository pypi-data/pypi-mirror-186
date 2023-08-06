"""
MessagePack functions.

For detailed information about MessagePack see `https://msgpack.org/index.html`.

These module contains default dumps and loads command as well as classes for
extended types implementation.

Extended types
--------------

Extended types allow you to serialize and deserialize python object using msgpack.
To set up your extended type the easiest way to inherit from :class:`.Serializable`
class and from :class:`.MsgpackType`, set an unique `ext_class_id` and regiser
it in `msgpack_types`.

.. code-block:: python

    class MyClass(Serializable, MsgpackType):

        ext_class_id = 42

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self._c = a + b

    from kaiju_tools.msgpack import msgpack_types

    msgpack_types.register_class(MyClass)


From now you can use it in your messages.

.. code-block:: python

    from kaiju_tools.msgpack import dumps, loads

    obj = MyClass(6, 6)
    msg = dumps(obj)
    obj = loads(msg)


If you want to further optimize packing (which is not always possible) you can
create your own pack and unpack methods.

.. code-block:: python

    import struct

    class MyClass(MsgpackType):

        ext_class_id = 42

        DATA_STRUCT = 'II'

        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b
            self._c = a + b

        def to_bytes(self):
            return struct.pack(self.DATA_STRUCT, self.a, self.b)

        @classmethod
        def from_bytes(cls, data):
            return cls(*struct.unpack(cls.DATA_STRUCT, data))


Functions
---------

"""


import abc
import calendar
import datetime
import uuid
from decimal import Decimal
from typing import Mapping
from types import SimpleNamespace

import msgpack
from msgpack import dumps as msgpack_dumps
from msgpack import loads as msgpack_loads

from kaiju_tools.class_registry import AbstractClassRegistry
from .abc import SerializerInterface
from .etc import MimeTypes

__all__ = (
    'MsgpackType', 'ReservedClassIDs', 'Types', 'msgpack_types',
    'dumps', 'loads', 'Serializer'
)


class MsgpackType(abc.ABC):
    """
    Serializable binary object.
    """

    ext_class_id: int  # must be set

    def repr(self) -> dict:
        raise NotImplementedError(
            'You either need to inherit from `kaiju_tools.serialization.Serializable`'
            ' or to set up your own `repr()` method or to set up you own'
            ' `pack_b` and `unpack_b` methods.')

    def to_bytes(self) -> bytes:
        """Pack object to bytes (you can use a struct here to optimize size)."""

        return dumps(self.repr())

    @classmethod
    def from_bytes(cls, data: bytes) -> 'MsgpackType':
        """Unpack bytes into object."""

        return cls(**loads(data))


class ReservedClassIDs:

    # reserved from 0 to 16 (incl.)

    uuid = 1
    frozenset = 2
    datetime = 3
    decimal = 4
    date = 5


class Types(AbstractClassRegistry):
    """Msgpack types registry."""

    base_classes = (MsgpackType,)

    @staticmethod
    def class_key(obj) -> int:
        """Determines a name by which a registered class will be referenced in
        the class mapping."""

        return obj.ext_class_id

    def _validate_class(self, obj):
        super()._validate_class(obj)
        key = self.class_key(obj)
        if not 16 < key < 128:
            raise ValueError('Msgpack ext type id allowed to be in range from 17 to 127 but got "%s".', key)


msgpack_types = Types(raise_if_exists=True)


def _default_types(obj):
    """Extended types serializer."""

    if isinstance(obj, uuid.UUID):
        return msgpack.ExtType(ReservedClassIDs.uuid, obj.bytes)
    elif isinstance(obj, datetime.datetime):
        return msgpack.ExtType(ReservedClassIDs.datetime, msgpack_dumps(calendar.timegm(obj.utctimetuple())))
    elif isinstance(obj, datetime.date):
        return msgpack.ExtType(ReservedClassIDs.date, msgpack_dumps(calendar.timegm(obj.timetuple())))
    elif isinstance(obj, (set, frozenset)):
        return msgpack.ExtType(ReservedClassIDs.frozenset, msgpack_dumps(tuple(obj), default=_default_types))
    elif isinstance(obj, MsgpackType):
        return msgpack.ExtType(obj.ext_class_id, obj.to_bytes())
    elif isinstance(obj, Mapping):
        return dict(obj)
    elif type(obj) == SimpleNamespace:
        return obj.__dict__
    elif type(obj).__name__ == 'Record':
        return dict(obj)
    elif type(obj) == Decimal:
        return msgpack.ExtType(ReservedClassIDs.decimal, msgpack_dumps(str(obj)))
    else:
        raise ValueError('Unsupported object type: %s.', type(obj))


def _ext_hook(code, data):
    """Extended types loader."""

    if code == ReservedClassIDs.uuid:
        return uuid.UUID(bytes=data)
    elif code == ReservedClassIDs.datetime:
        return datetime.datetime.utcfromtimestamp(msgpack_loads(data))
    elif code == ReservedClassIDs.date:
        return datetime.date.fromtimestamp(msgpack_loads(data))
    elif code == ReservedClassIDs.frozenset:
        return frozenset(msgpack_loads(data))
    elif code == ReservedClassIDs.decimal:
        return Decimal(msgpack_loads(data))
    elif code in msgpack_types:
        cls = msgpack_types[code]
        return cls.from_bytes(data)
    else:
        raise ValueError(code)


def dumps(*args, **kws):
    return msgpack_dumps(*args, default=_default_types, **kws)


def loads(*args, **kws):
    return msgpack_loads(*args, ext_hook=_ext_hook, **kws)


class Serializer(SerializerInterface):

    mime_type = MimeTypes.msgpack
    ext_hook = _ext_hook
    default = _default_types

    @classmethod
    def loads(cls, *args, **kws):
        return msgpack_loads(*args, ext_hook=cls.ext_hook, **kws)

    @classmethod
    def dumps(cls, *args, **kws):
        return msgpack_dumps(*args, default=cls.default, **kws)

    @classmethod
    def dumps_bytes(cls, *args, **kws):
        return msgpack_dumps(*args, default=cls.default, **kws)
