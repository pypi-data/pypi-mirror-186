import abc

__all__ = ('SerializerInterface',)


class SerializerInterface(abc.ABC):
    """Abstract serializer interface that should be used by clients/servers to
    process raw messages."""

    mime_type = None  # you should define an appropriate mime type here

    @classmethod
    @abc.abstractmethod
    def loads(cls, data, *args, **kws):
        pass

    @classmethod
    @abc.abstractmethod
    def dumps(cls, data, *args, **kws) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def dumps_bytes(cls, data, *args, **kws) -> bytes:
        pass
