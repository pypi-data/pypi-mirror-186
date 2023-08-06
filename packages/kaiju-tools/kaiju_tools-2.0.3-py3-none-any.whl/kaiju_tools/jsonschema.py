"""
JSONSchema wrapper classes.

You can create a JSONSchema spec using these ones.

.. code-block:: python

    import fastjsonschema

    schema = Object({
        'id': Integer(minimum=1, title='row id'),
        'tags': Array(String(title='tag name'), minItems=1)
    })

    validator = fastjsonschema.compile(schema)
    validator({'id': 11, 'tags': ['a', 'b', 'c']})


Ideally you may be able to unpack a real jsonschema into these classes's inits
because param names (should) match the jsonschema specification.

See classes description for more info.

Classes
-------

"""

import abc
from functools import partial
from typing import Union, Dict, List, Collection

from fastjsonschema import compile
from fastjsonschema.exceptions import JsonSchemaException

from .serialization import Serializable

__all__ = (

    'custom_formatters', 'compile_schema',

    # types

    'JSONSchemaObject', 'Enumerated',
    'Boolean', 'String', 'Number', 'Integer', 'Array', 'Object', 'Generic',

    # keywords

    'JSONSchemaKeyword', 'AnyOf', 'OneOf', 'AllOf', 'Not',

    # aliases

    'GUID', 'Date', 'DateTime', 'Null', 'Constant',

)


class JSONSchemaObject(Serializable, abc.ABC):
    """
    You shouldn't use this class directly. Instead use on of the following
    non-abstract classes.
    """

    __slots__ = ('default', 'title', 'description', 'examples', 'enum', 'nullable')

    def __init__(
            self, title: str = None, description: str = None, default=None,
            examples: list = None, enum: list = None, nullable: bool = False):
        self.default = default
        self.title = title
        self.description = description
        self.examples = examples
        self.enum = enum
        self.nullable = nullable

    def repr(self) -> dict:
        """Here should be your object JSON Schema definition."""

        data = {
            key: getattr(self, key, None)
            for key in self.__slots__
            if not key.startswith('_') and getattr(self, key, None) is not None
        }
        if getattr(self, 'nullable', None):  # hack to support OpenAPI `nullable` kw
            data = {'oneOf': [Null.repr(), data]}  # noqa
        return data


class Boolean(JSONSchemaObject):
    """
    Boolean `True` or `False`.

    :param default: optional default value for non-existing params
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    """

    __slots__ = ('default', 'title', 'description', 'nullable')

    def __init__(self, title: str = None, description: str = None, default=None, nullable=False):
        self.default = default
        self.title = title
        self.description = description
        self.nullable = nullable

    def repr(self) -> dict:
        return {
            'type': 'boolean',
            **super().repr()
        }


class Enumerated(JSONSchemaObject):
    """
    Value can be one from the list. Use `Enumerated` type if you need to
    have different data types in one enum. Otherwise it's recommended to use
    a specific data type with `enum=` argument passed into it.

    :param enum: required list of allowed values
    :param default: optional default value for non-existing params
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    """

    __slots__ = ('default', 'title', 'description', 'enum')

    def __init__(self, enum: list, title: str = None, description: str = None, default=None):
        self.default = default
        self.title = title
        self.description = description
        self.enum = enum


class String(JSONSchemaObject):
    """
    Text/string data type.

    :param default: optional default value for non-existing params
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    :param examples: optional list of examples
    :param enum: optional list of allowed values for this parameter
    :param minLength: optional minimum string length
    :param maxLength: optional maximum string length
    :param pattern: optional regex validation pattern
    :param format: optional specific string format (see `String.STRING_FORMATS`)
    """

    STRING_FORMATS = frozenset({
        'date-time', 'time', 'date',
        'email', 'idn-email', 'hostname', 'idn-hostname', 'ipv4', 'ipv6',
        'uri', 'uri-reference', 'iri', 'iri-reference', 'regex'
    })

    __slots__ = tuple([
        *JSONSchemaObject.__slots__, 'minLength', 'maxLength', 'pattern', 'format',
    ])

    def __init__(
            self, title: str = None, description: str = None, default: str = None,
            examples: List[str] = None, enum: List[str] = None, minLength: int = None,
            maxLength: int = None, pattern: str = None, format: str = None,
            nullable=None):
        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, nullable=nullable)
        self.minLength = minLength
        self.maxLength = maxLength
        self.pattern = pattern
        if format and format not in self.STRING_FORMATS:
            raise JsonSchemaException(
                'Invalid string format "%s".'
                'Must be one of: "%s".' % (format, list(self.STRING_FORMATS)))
        self.format = format

    def repr(self) -> dict:
        return {
            'type': 'string',
            **super().repr()
        }


class DateTime(JSONSchemaObject):
    """
    Datetime string alias.
    """

    __slots__ = tuple([*JSONSchemaObject.__slots__, 'format'])

    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.format = 'date-time'


class Date(JSONSchemaObject):
    """
    Date string alias.
    """

    __slots__ = tuple([*JSONSchemaObject.__slots__, 'format'])

    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.format = 'date'


class GUID(JSONSchemaObject):
    """
    UUID string alias.
    """

    __slots__ = tuple([*JSONSchemaObject.__slots__, 'format'])

    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.format = 'uuid'


class Constant(Enumerated):
    """
    Value is constant.

    :param const: required value of a constant
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    """

    __slots__ = tuple([*Enumerated.__slots__, 'type'])

    def __init__(self, const, title: str = None, description: str = None, type: str = None):
        super().__init__(enum=[const], title=title, description=description)
        self.type = type


class _Null(Constant):
    """
    Null value only.

    Use :class:`.Null` instead of this.
    """

    __slots__ = Constant.__slots__

    def __init__(self):
        super().__init__(const=None, title=None, description=None)


Null = _Null()


class Number(JSONSchemaObject):
    """
    Numeric data type (use it for both float or integer params).

    :param default: optional default value for non-existing params
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    :param examples: optional list of examples
    :param enum: optional list of allowed values for this parameter
    :param multipleOf: optional divider of the value
    :param minimum: optional minimum value
    :param maximum: optional maximum value
    :param exclusiveMinimum: optional
    :param exclusiveMaximum: optional
    """

    __slots__ = tuple([
        *JSONSchemaObject.__slots__, 'multipleOf', 'minimum', 'exclusiveMinimum',
        'maximum', 'exclusiveMaximum'
    ])

    def __init__(
            self, title: str = None, description: str = None, default: float = None,
            examples: List[float] = None, enum: List[float] = None,
            multipleOf: float = None,
            minimum: float = None, maximum: float = None,
            exclusiveMinimum: float = None,
            exclusiveMaximum: float = None, nullable=None):

        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, nullable=nullable)
        self.multipleOf = multipleOf
        self.minimum = minimum
        self.maximum = maximum
        self.exclusiveMinimum = exclusiveMinimum
        self.exclusiveMaximum = exclusiveMaximum

    def repr(self) -> dict:
        return {
            'type': 'number',
            **super().repr()
        }


class Integer(Number):
    """
    Integer type.

    :param default: optional default value for non-existing params
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    :param examples: optional list of examples
    :param enum: optional list of allowed values for this parameter
    :param multipleOf: optional divider of the value
    :param minimum: optional minimum value
    :param maximum: optional maximum value
    :param exclusiveMinimum: optional
    :param exclusiveMaximum: optional
    """

    __slots__ = Number.__slots__

    def __init__(
            self, title: str = None, description: str = None, default: int = None,
            examples: List[int] = None, enum: List[int] = None,
            multipleOf: int = None, minimum: int = None, maximum: int = None,
            exclusiveMinimum: int = None,
            exclusiveMaximum: int = None, nullable=None):
        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, multipleOf=multipleOf,
            minimum=minimum, maximum=maximum, exclusiveMinimum=exclusiveMinimum,
            exclusiveMaximum=exclusiveMaximum, nullable=nullable)

    def repr(self) -> dict:
        data = super().repr()
        data['type'] = 'integer'
        return data


class Array(JSONSchemaObject):
    """
    An array, list, set or tuple definition (depends on params).

    :param items: optional schema of contained items, you can pass a list
        for a tuple schema definition
    :param contains: optional condition on item that must present in the array
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    :param examples: optional list of examples
    :param additionalItems: optional defines if additional items are allowed
    :param uniqueItems: optional defines if only unique items are allowed
    :param minItems: optional min length of an array
    :param maxItems: optional max length of an array
    """

    __slots__ = tuple([
        *JSONSchemaObject.__slots__, 'items', 'contains',
        'additionalItems', 'uniqueItems', 'minItems', 'maxItems'
    ])

    def __init__(
            self, items: Union[JSONSchemaObject, Collection[JSONSchemaObject], dict, Collection[dict]] = None,
            contains: Union[dict, JSONSchemaObject] = None, title: str = None,
            description: str = None, examples: list = None, additionalItems: bool = None,
            uniqueItems: bool = None, minItems: int = None, maxItems: int = None,
            nullable=None):

        super().__init__(
            title=title, description=description, default=None,
            examples=examples, enum=None, nullable=nullable)

        if items:
            if isinstance(items, JSONSchemaObject):
                self.items = items.repr()
            elif isinstance(items, dict):
                self.items = items
            elif isinstance(items, Collection):
                self.items = []
                for item in items:
                    if isinstance(item, JSONSchemaObject):
                        item = item.repr()
                    self.items.append(item)
        else:
            self.items = None

        if contains:
            if isinstance(contains, JSONSchemaObject):
                self.contains = contains.repr()
            elif isinstance(items, dict):
                self.contains = contains
        else:
            self.contains = None

        self.additionalItems = additionalItems
        self.uniqueItems = uniqueItems
        self.minItems = minItems
        self.maxItems = maxItems

    def repr(self) -> dict:
        return {
            'type': 'array',
            **super().repr(),
        }


class Object(JSONSchemaObject):
    """
    A JSON object (dictionary) definition.

    This class usually will be a parent class for your validation schema.

    :param properties: optional field definitions
    :param patternProperties: optional field pattern definitions (can validate
        multiple fields by regex name patterns)
    :param propertyNames:
    :param contains: optional condition on item that must present in the array
    :param title: optional parameter title doc
    :param description: optional parameter description doc
    :param examples: optional list of examples
    :param additionalItems: optional defines if additional items are allowed
    :param uniqueItems: optional defines if only unique items are allowed
    :param minItems: optional min length of an array
    :param maxItems: optional max length of an array
    :param kws: you can pass properties as keyword args as well
    """

    __slots__ = tuple([
        *JSONSchemaObject.__slots__,
        'properties', 'propertyNames', 'required', 'patternProperties',
        'additionalProperties', 'minProperties', 'maxProperties'
    ])

    def __init__(
            self, properties: Union[Dict[str, JSONSchemaObject], Dict[str, dict]] = None,
            patternProperties: Union[Dict[str, JSONSchemaObject], Dict[str, dict]] = None,
            propertyNames: dict = None,
            additionalProperties: bool = None, minProperties: int = None,
            maxProperties: int = None, required: List[str] = None,
            title: str = None, enum=None,
            description: str = None, default=None,
            examples: list = None, nullable=None, **kws):

        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, nullable=nullable)

        _properties = {}
        if kws:
            _properties.update(kws)
        if properties:
            _properties.update(properties)

        if _properties:
            self.properties = {}
            for key, value in _properties.items():
                if isinstance(value, JSONSchemaObject):
                    value = value.repr()
                self.properties[key] = value
        else:
            self.properties = None

        if patternProperties:
            self.patternProperties = {}
            for key, value in patternProperties.items():
                if isinstance(value, JSONSchemaObject):
                   value = value.repr()
                self.patternProperties[key] = value
        else:
            self.patternProperties = None

        if propertyNames is not None and 'pattern' not in propertyNames:
            raise JsonSchemaException('propertyNames param must have "pattern" attribute.')
        self.propertyNames = propertyNames

        self.additionalProperties = additionalProperties
        self.minProperties = minProperties
        self.maxProperties = maxProperties

        self.required = required

    def repr(self) -> dict:
        return {
            'type': 'object',
            **super().repr(),
        }


class Generic(JSONSchemaObject):
    """
    Use this for specific or partial conditions. It's recommended to use
    specific types instead of the generic one when possible.
    """

    def __init__(
            self, title: str = None, description: str = None, default=None,
            examples: list = None, enum: list = None, nullable=None, **kws):
        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, nullable=nullable)
        for key, value in kws.items():
            setattr(self, key, value)


class JSONSchemaKeyword(JSONSchemaObject, abc.ABC):
    """
    Abstract class for JSON Schema specific logical keywords.
    """

    __slots__ = tuple([*JSONSchemaObject.__slots__, '_items'])

    def __init__(
            self, *items: Union[JSONSchemaObject, dict],
            title: str = None, description: str = None, default=None,
            examples: list = None, enum: list = None, nullable=None):

        super().__init__(
            title=title, description=description, default=default,
            examples=examples, enum=enum, nullable=nullable)

        if items:
            self._items = []
            for item in items:
                if isinstance(item, JSONSchemaObject):
                    item = item.repr()
                self._items.append(item)
        else:
            raise JsonSchemaException('JSON Schema keyword items must present')


class AnyOf(JSONSchemaKeyword):
    """
    The given data must be valid against any (one or more) of the given sub-schemas.
    """

    __slots__ = JSONSchemaKeyword.__slots__

    def repr(self) -> dict:
        return {
            **super().repr(),
            'anyOf': self._items
        }


class OneOf(JSONSchemaKeyword):
    """
    The given data must be valid against exactly one of the given sub-schemas.
    """

    __slots__ = JSONSchemaKeyword.__slots__

    def repr(self) -> dict:
        return {
            **super().repr(),
            'oneOf': self._items
        }


class AllOf(JSONSchemaKeyword):
    """
    The given data must be valid against all of the given sub-schemas.
    """

    __slots__ = JSONSchemaKeyword.__slots__

    def repr(self) -> dict:
        return {
            **super().repr(),
            'allOf': self._items
        }


class Not(JSONSchemaKeyword):
    """
    Reverse the condition.
    """

    __slots__ = ('_item',)

    def __init__(self, item: Union[JSONSchemaObject, dict]):
        """
        :param items: condition to be reversed
        """

        if isinstance(item, JSONSchemaObject):
            self._item = item.repr()
        else:
            self._item = item

    def repr(self):
        return {
            'not': self._item
        }


custom_formatters = {
    'uuid': r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$'
} # these are used by the fastjsonschema compiler to validate some specific data types


def compile_schema(validator, formats=None):
    if formats is None:
        formats = custom_formatters
    if isinstance(validator, JSONSchemaObject):
        validator = validator.repr()
    return compile(validator, formats=formats)
