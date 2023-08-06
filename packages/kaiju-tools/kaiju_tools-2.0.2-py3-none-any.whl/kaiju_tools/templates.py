"""Working with data templates and conditions."""

import abc
from ast import literal_eval
from dataclasses import dataclass
from datetime import datetime
from fnmatch import fnmatch
from os import urandom
from random import randint, random
from typing import Any, Union, ClassVar, List, Iterable, Container, Sequence
from numbers import Real
from uuid import uuid4

from kaiju_tools.mapping import get_field
from kaiju_tools.class_registry import AbstractClassRegistry
from kaiju_tools.serialization import Serializable

__all__ = [
    'COMPARISON_FUNCTIONS',
    'Condition',
    'Operator',
    'TEMPLATE_FUNCTIONS',
    'OPERATORS',
    'OperatorEval',
    'OperatorFormat',
    'OperatorSelect',
    'OperatorExec',
    'Template',
    'Operators'
]

# >> comparison_functions
COMPARISON_FUNCTIONS = {
    'gt': lambda args: isinstance(args[0], Real) and isinstance(args[1], Real) and args[0] > args[1],
    'lt': lambda args: isinstance(args[0], Real) and isinstance(args[1], Real) and args[0] < args[1],
    'ge': lambda args: isinstance(args[0], Real) and isinstance(args[1], Real) and args[0] >= args[1],
    'le': lambda args: isinstance(args[0], Real) and isinstance(args[1], Real) and args[0] <= args[1],
    'eq': lambda args: args[0] == args[1],
    'ne': lambda args: args[0] != args[1],
    'has': lambda args: isinstance(args[0], Container) and args[1] in args[0],
    'in': lambda args: isinstance(args[1], Container) and args[0] in args[1],
    'match': lambda args: fnmatch(str(args[0]), str(args[1])),
}
# << comparison_functions


# >> functions
TEMPLATE_FUNCTIONS = {
    'str': lambda args: str(args[0]),
    'len': lambda args: len(args[0]),
    'int': lambda args: int(args[0]),
    'bool': lambda args: bool(args[0]),
    'datetime': lambda args: datetime.fromisoformat(args[0]),
    'date': lambda args: datetime.fromisoformat(args[0]).date(),
    'sum': sum,
    'max': max,
    'min': min,
    'all': all,
    'any': any,
    'first': lambda args: args[0],
    'last': lambda args: args[-1],
    'uuid4': lambda args: uuid4(),
    'utcnow': lambda args: datetime.utcnow(),
    'now': lambda args: datetime.now(),
    'now_date': lambda args: datetime.now().date(),
    'timestamp': lambda args: datetime.now().timestamp(),
    'random': lambda args: random(),
    'randint': lambda args: randint(args[0], args[1]),
    'urandom': lambda args: urandom(args[0]),
    'capitalize': lambda args: args[0].capitalize(),
    'upper': lambda args: args[0].upper(),
    'lower': lambda args: args[0].lower(),
    'split': lambda args: args[1].split(args[0]),
    'join': lambda args: args[0].join(args[1:]),
}
# << functions


@dataclass
class Condition(Serializable):
    """Condition object.

    Check a dictionary-like structure against a defined condition schema.

    Basic rules: there is a mapping with keys matching keys in the data structure you're checking (nested
    keys are allowed and extracted using `extract_field` function). Values should contain a mapping of
    <operator>: <comparison value> for each key.
    All operators and all key conditions in mappings are combined by logical AND. All operators or conditions
    inside a list are combined using logical OR.

    See examples:

    >>> data = {'value': True, 'nested': {'value': 42, 'list': [1, 2, 3]}, 'objects': [{'id': 0}, {'id': 2}, {'id': 9}]}

    # AND conditions

    >>> Condition({'value': True, 'nested.value': {'gt': 41, 'in': [42, 43]}, 'nested.list': {'has': 3}})(data)
    True

    # condition with a nested attribute aggregation

    >>> Condition({'objects.id': {'has': 9}})(data)
    True

    # OR conditions for a single key

    >>> Condition({'nested.list': [{'has': 3}, {'eq': True}]})(data)
    True

    # OR conditions for multiple keys

    >>> Condition([{'value': True, 'nested.value': {'lt': 42}}, {'nested.list': {'has': 2}}])(data)
    True

    # wildcards

    >>> Condition({'nested.value': {'match': '4*'}})(data)
    True

    # NOT keyword for a single key

    >>> Condition({'nested.list': {'not': [{'has': 5}, {'eq': False}]}})(data)
    True

    # NOT keyword for multiple keys

    >>> Condition({'not': [{'value': False}, {'nested.value': 43}]})(data)
    True

    # NONE for not existing values

    >>> Condition({'not_present': None})(data)
    True

    """

    class Definitions:
        operator_not: str = 'not'
        default_condition: str = 'eq'

    functions = COMPARISON_FUNCTIONS
    schema: Union[dict, List[dict], 'Template']

    def __call__(self, data: Union[dict, Iterable[dict]], /) -> bool:
        """Check condition against provided data."""
        schema = self.schema.fill(data) if isinstance(self.schema, Template) else self.schema
        return self._check(schema, data)

    def _check(self, conditions: Union[dict, Iterable[dict]], data: dict) -> bool:
        """Check conditions."""
        if type(conditions) is dict:
            if self.Definitions.operator_not in conditions:
                return not self._check(conditions[self.Definitions.operator_not], data)  # noqa pycharm why?
            else:
                return all((
                    self._check_condition(condition, get_field(data, key, default=None))  # noqa pycharm why?
                    for key, condition in conditions.items()
                ))
        else:
            return any(self._check(sub_cond, data) for sub_cond in conditions)

    def _check_condition(self, condition: Any, value: Any, reverse: bool = False) -> bool:
        if type(condition) is dict:
            if self.Definitions.operator_not in condition:
                condition = condition[self.Definitions.operator_not]
                result = self._check_condition(condition, value, reverse=True)
            else:
                result = all((self.functions[op]((value, comp)) for op, comp in condition.items()))
        elif type(condition) in {list, tuple}:
            result = any(self._check_condition(sub_cond, value) for sub_cond in condition)
        else:
            result = self.functions[self.Definitions.default_condition]((value, condition))
        return not result if reverse else result


@dataclass
class Operator(abc.ABC):
    """Base operator object.

    All operators must inherit from this base class.
    """

    sign: ClassVar[str]
    template: 'Template'
    args: Sequence

    def __post_init__(self):
        self.template = self.template
        if not self.args:
            raise ValueError('No arguments provided')

    def __call__(self, data: dict):
        """Call an operator with dynamic data."""
        args = tuple(self._eval_args(data))
        return self._eval(args, data)

    @abc.abstractmethod
    def _eval(self, args: tuple, data: dict):
        """Evaluate arguments using provided data.

        This method should contain operator-specific evaluation logic.

        :param args: a tuple of already evaluated arguments
        :param data: dynamic data
        :returns: evaluated operator value
        """
        ...

    def _eval_args(self, data: dict):
        for arg in self.args:
            if isinstance(arg, Operator):
                arg = arg(data)
            yield arg


@dataclass
class OperatorSelect(Operator):
    """Selection operator."""

    sign = 's'

    def _eval(self, args: tuple, data: dict):
        arg = args[0]
        if len(args) > 1:
            default = args[1]
            if not isinstance(self.args[1], Operator):
                default = literal_eval(default)
        else:
            default = self.template.Definitions.empty_default
        result = get_field(data, arg, delimiter=self.template.Definitions.key_delimiter, default=default)
        return result


@dataclass
class OperatorFormat(Operator):
    """String format operator."""

    class _FormatDict(dict):

        def __init__(self, *args, template: 'Template', **kws):
            super().__init__(*args, **kws)
            self.default = template.Definitions.fmt_empty_default
            self.delimiter = template.Definitions.fmt_key_delimiter

        def __getitem__(self, item):
            if item in self:
                return dict.__getitem__(self, item)
            return get_field(self, item, default=self.default, delimiter=self.delimiter)

    sign = 'f'

    def _eval(self, args: tuple, data: dict):
        data = self._FormatDict(data, template=self.template)
        result = self.template.Definitions.fmt_join_delimiter.join(arg.format_map(data) for arg in args)
        return result


@dataclass
class OperatorEval(Operator):
    """Literal evaluation operator."""

    sign = 'e'

    def _eval(self, args: tuple, data: dict):
        result = tuple(literal_eval(arg) for arg in args)
        if len(args) == 1:
            result = result[0]
        return result


@dataclass
class OperatorExec(Operator):
    """Function execution operator."""

    sign = 'x'

    # >> functions_call
    def _eval(self, args: tuple, data: dict):
        func_name, args = args[0], args[1:]
        func_args = []
        for arg, value in zip(self.args[1:], args):
            if isinstance(arg, str):
                value = literal_eval(value)
            func_args.append(value)
        f = self.template.functions[func_name]
        return f(func_args)

# >> functions_call


class Operators(AbstractClassRegistry):

    base_classes = [Operator]

    def class_key(self, obj) -> str:
        return obj.sign


OPERATORS = Operators()
OPERATORS.register_classes_from_namespace(locals())


@dataclass
class Template(Serializable):
    """Template object is able to fill a template with arbitrary data.

    Examples
    ________

    Basic templating:

    >>> t = Template({
    ... 'value': '[test]',
    ... 'values': ['[inner.value]', '[inner.value]'],
    ... 'default': '[unknown:42]',
    ... 'default_str': '[unknown:"test"]',
    ... 'default_op': '[unknown:[!x:bool:0]]'
    ... })
    >>> t({'test': 42, 'inner': {'value': 41}})
    {'value': 42, 'values': (41, 41), 'default': 42, 'default_str': 'test', 'default_op': False}

    Nested templates:

    >>> t = Template('[[inner.key]]')
    >>> t({'inner': {'key': 'me'}, 'me': 'dogs'})
    'dogs'

    Eval:

    >>> t = Template('[!e:[key]]')
    >>> t({'key': 'True'})
    True

    Format:

    >>> t = Template('[!f:{obj-name} price is {obj-price}]')
    >>> t({'obj': {'name': 'dogs', 'price': 42}})
    'dogs price is 42'

    Format join:

    >>> t = Template('[!f:this is {obj_1}:and this is {obj_2}]')
    >>> t({'obj_1': 'dogs', 'obj_2': 'cats'})
    'this is dogs,and this is cats'

    Functions:

    >>> t = Template({'all': '[!x:all:[a]:[b]:0]', 'any': '[!x:any:[a]:[b]:0]'})
    >>> t({'a': 1, 'b': 2})
    {'all': False, 'any': True}

    Nested functions:

    >>> t = Template('[!x:sum:[a]:[!x:int:[b]]:0]')
    >>> t({'a': 1, 'b': 3.14})
    4

    Quotation:

    >>> t = Template("[!f:`[{obj-name}]: {obj-price}`]")
    >>> t({'obj': {'name': 'dogs', 'price': 42}})
    '[dogs]: 42'

    """

    class Definitions:
        operator_brackets: str = '[]'
        operator_sign: str = '!'
        operator_delimiter: str = ':'
        key_delimiter: str = '.'
        fmt_key_delimiter: str = '-'
        empty_default: Union[Exception, str] = KeyError
        fmt_empty_default: Union[Exception, str] = '???'
        fmt_join_delimiter: str = ','
        default_operator: str = 's'
        escape_quote = '`'

    functions = TEMPLATE_FUNCTIONS
    operators = OPERATORS
    schema: Union[dict, list, tuple, str]

    def __post_init__(self):
        self._schema = self._parse_value(self.schema)

    def __call__(self, data: dict, /):
        return self.fill(data)

    def fill(self, data: dict, /):
        """Fill template with dynamic data."""
        return self._fill_value(self._schema, data)

    def _fill_value(self, value, data: dict):
        if isinstance(value, dict):
            return {k: self._fill_value(v, data) for k, v in value.items()}
        elif isinstance(value, Iterable) and not isinstance(value, str):
            return tuple(self._fill_value(v, data) for v in value)
        elif isinstance(value, Operator):
            return value(data)
        else:
            return value

    def _parse_value(self, value, key: str = None):
        if isinstance(value, dict):
            value = {k: self._parse_value(v, key=k) for k, v in value.items()}
        elif isinstance(value, str):
            value = self._parse_string(value, key=key)
        elif isinstance(value, Iterable):
            value = tuple(self._parse_value(v, key=key) for v in value)
        return value

    def _parse_string(self, s: str, key: str = None) -> Union['Operator', str]:

        if not s:
            return s

        bl, br = self.Definitions.operator_brackets
        bls, blr = s[0] == bl, s[-1] == br

        if not bls and not blr:
            if s[0] == self.Definitions.escape_quote and s[-1] == self.Definitions.escape_quote:
                s = s[1:-1]
            return s
        elif not bls or not blr:
            raise ValueError(f'Unbalanced brackets in template: key={key}, value={s}.')

        s = s[1:-1]
        counter = 0
        x = 0
        args = []
        quoted = False

        for n, v in enumerate(s):
            if v == self.Definitions.escape_quote:
                quoted = not quoted
            elif v == bl and not quoted:
                counter += 1
            elif v == br and not quoted:
                counter -= 1
            if v == self.Definitions.operator_delimiter and not quoted:
                if counter == 0:
                    args.append(self._parse_string(s[x:n], key=key))
                    x = n + 1

        s = s[x : len(s)]  # noqa
        if s:
            args.append(self._parse_string(s, key=key))

        if isinstance(args[0], str) and args[0].startswith(self.Definitions.operator_sign):
            op = args[0][1:]
            args = args[1:]
        else:
            op = self.Definitions.default_operator

        op = self.operators[op](template=self, args=args)  # noqa pycharm
        return op
