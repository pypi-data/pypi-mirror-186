import pytest

from ..serialization import Comparable, Hashable


@pytest.mark.unit
def test_serialization(logger):

    class C(Comparable):

        serializable_attrs = ('a', 'b')

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.c = a + b

    class D(Comparable):

        __slots__ = ('a', 'b', '_c')

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self._c = a + b

        @property
        def c(self):
            return self._c

    class H(Hashable):

        __slots__ = ('a', 'b', 'c')
        serializable_attrs = ('a', 'b')

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.c = a + b

    for cls in (C, D, H):
        logger.info('testing subclass of %s ...', cls.__bases__[-1].__name__)

        logger.info(' - construction')
        c = cls(1, 2)
        d = cls(**dict(c))
        e = cls(1, 3)

        logger.info(' - comparison')
        assert d.c == c.c
        assert c == d
        assert e != c

        logger.info(' - serialization / deserialization')
        x = cls.from_json(d.to_json())
        assert x == d

        if issubclass(cls, Hashable):
            logger.info(' - hashing')
            assert c.uuid == d.uuid
            _map = {c: True}
            assert _map[d]

        logger.info('')
