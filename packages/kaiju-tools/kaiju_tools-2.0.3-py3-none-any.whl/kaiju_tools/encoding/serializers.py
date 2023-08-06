from kaiju_tools.class_registry import AbstractClassRegistry
from .abc import SerializerInterface

from .msgpack import Serializer as MsgPackSerializer
from .json import Serializer as JSONSerializer

__all__ = ('Serializers', 'serializers')


class Serializers(AbstractClassRegistry):
    """
    Message serializer registry class.
    """

    base_classes = (SerializerInterface,)

    @staticmethod
    def class_key(obj: SerializerInterface) -> str:
        return obj.mime_type


serializers = Serializers(raise_if_exists=True)  #: message serializer registry
serializers.register_class(JSONSerializer)
serializers.register_class(MsgPackSerializer)
