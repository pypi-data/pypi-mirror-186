from weakref import proxy, ProxyType
from base64 import b64encode
from copy import deepcopy
from typing import *

from ..serialization import Serializable, Hashable, Comparable
from ..mapping import recursive_update

__all__ = ('Field', 'Metadata', 'Index')


class Metadata:
    """Метаданные ES.

    Этот объект можно использовать для получения списка всех индексов (для
    этого при инициализации индекса нужно передать объект `Metadata` в соотв.
    параметр).
    Также его можно использовать для хранения общих настроек у индексов.
    """

    def __init__(self, settings: dict = None):
        """
        :param settings: общие настройки для всех индексов
        """

        self.indices = []
        self.index_mapping = {}
        self.settings = settings if settings else {}

    def register(self, index):
        self.indices.append(index)
        self.index_mapping[index.mapping.name] = index
        index.settings = recursive_update(deepcopy(self.settings), index.settings)

    def __delitem__(self, item):
        i = self.indices.index(item)
        del self.indices[i]
        del self.index_mapping[item.mapping.name]

    def __contains__(self, item):
        return item in self.indices

    def __getitem__(self, item):
        return self.index_mapping[item]

    def __iter__(self):
        return iter(self.indices)


class Field(Serializable):
    """Поле индекса."""

    def _pass(value):
        return value

    def _to_date_range(value: Union[dict, list]):
        if isinstance(value, dict):
            return {k: str(v) for k, v in value.items()}
        else:
            _gte, _lte = value
            return {'gte': str(_gte), 'lte': str(_lte)}

    def _to_byte(value: str):
        return b64encode(str(value).encode('utf-8'))

    def _to_int_range(value: Union[dict, list, tuple]):
        if isinstance(value, dict):
            return {k: int(v) for k, v in value.items()}
        else:
            _gte, _lte = value
            return {'gte': int(_gte), 'lte': int(_lte)}

    def _to_float_range(value: Union[dict, list, tuple]):
        if isinstance(value, dict):
            return {k: float(v) for k, v in value.items()}
        else:
            _gte, _lte = value
            return {'gte': float(_gte), 'lte': float(_lte)}

    def _to_geo_point(value: Union[list, dict]):
        if isinstance(value, dict):
            return {'lon': value['lon'], 'lat': value['lat']}
        else:
            return {'lon': value[0], 'lat': value[1]}

    data_types = {
        frozenset((None,)): _pass,
        frozenset(('keyword', 'text')): str,
        frozenset(('long', 'integer', 'short', 'byte')): int,
        frozenset(('double', 'float', 'half_float', 'scaled_float')): float,
        frozenset(('date',)): str,
        frozenset(('boolean',)): bool,
        frozenset(('binary',)): _to_byte,
        frozenset(('object',)): dict,
        frozenset(('nested',)): list,
        frozenset(('integer_range', 'long_range')): _to_int_range,
        frozenset(('float_range', 'double_range')): _to_float_range,
        frozenset(('date_range',)): _to_date_range,
        frozenset(('geo_point',)): _to_geo_point
    }

    ranged_types = {
        'long', 'integer', 'short', 'byte', 'double', 'float', 'half_float',
        'scaled_float', 'date', 'integer_range', 'long_range',
        'float_range', 'double_range', 'date_range'
    }

    def __init__(self, name: str, type: str = None, meta: dict = None, **settings):
        """Создает новое поле индекса.

        :param name: имя поля
        :param type: тип данных (должен соответствовать типу в ES), см. `Field.data_types`
        :param meta: field metadata
        :param settings: другие настройки поля (как в ES)
        """

        self.name = name

        for keys, normalizer in self.data_types.items():
            if type in keys:
                self._normalizer = normalizer
                self.type = type
                break
        else:
            raise ValueError('Неизвестный тип данных %s для поля индекса.' % type)

        self.settings = settings

        if type in {'object', 'nested'}:
            self._has_properties = True
            properties = self.settings.pop('properties', {})
            if isinstance(properties, dict):
                self._fields = {name: Field(name, **kws) for name, kws in properties.items()}
            else:
                self._fields = {field.name: field for field in properties}
        else:
            self._has_properties = False

        self.meta = {} if meta is None else meta

        super().__init__()

    def __str__(self):
        return self.name

    def __call__(self, value):
        """Нормализует значение в соответствии с типом данных поля."""

        if isinstance(value, dict):
            if self._has_properties:
                return {
                    self._fields[key](v)
                    for key, v in value.items()
                }
            else:
                return {key: self(v) for key, v in value.items()}
        elif isinstance(value, Collection) and not isinstance(value, str):
            return [self(v) for v in value]
        else:
            return self._normalizer(value)

    def repr(self):
        """Репрезентация поля в формате ES."""

        r = {
            **self.settings
        }
        if self.type:
            r['type'] = self.type
        if self._has_properties:
            r['properties'] = {field.name: field.repr() for field in self._fields.values()}
        if self.meta:
            r['meta'] = self.meta
        return r


class Mapping(Hashable):
    """Мэппинг для документа в индексе."""

    def __init__(
            self, properties: Union[dict, Collection[Field]], index=None,
            _meta: dict = None, **settings):
        """
        :param properties: поля мэппинга (можно передать как dict объект в формате
            ES так и список из объектов `Field`
        :param index: обратная ссылка на индекс, в котором используется мэппинг
        :param _meta: метаданные (любые в формате JSON)
        :param settings: прочие настройки мэппинга как в ES
        """

        self._index = proxy(index)
        self.name = '_mapping'
        if isinstance(properties, dict):
            self._fields = {
                name: Field(name, **kws) for name, kws in properties.items()
            }
        else:
            self._fields = {field.name: field for field in properties}
        self._settings = settings
        self._meta = _meta if _meta else {}
        self._dynamic = settings.get('dynamic', True)
        super().__init__()

    def __call__(self, data: dict):
        """Нормализует значение в соответствии с типом данных документа."""

        result = {}
        for k, v in data.items():
            if k in self._fields:
                result[k] = self._fields[k](v)
            elif self._dynamic:
                result[k] = v
            else:
                raise ValueError('В индексе запрещены динамические поля.')
        return result

    def __str__(self):
        return self.name

    def __rtruediv__(self, other):
        """Строит URI до мэппинга."""

        return f'{other}/{self.name}'

    def __truediv__(self, other) -> str:
        """Строит URI до мэппинга."""

        if self._index:
            return self._index / f'{self.name}/{other}'
        else:
            return f'{self.name}/{self.name}/{other}'

    @property
    def meta(self):
        return self._meta

    @property
    def fields(self):
        return self._fields

    @property
    def properties(self):
        return {field.name: field.repr() for field in self._fields.values()}

    def repr(self):
        """Репрезентация мэппинга в формате ES."""

        _meta = dict(self._meta)
        _meta['hash'] = self.uuid

        return {
            '_meta': _meta,
            'properties': self.properties,
            **self._settings
        }

    def _hash(self) -> dict:
        return {
            'properties': self.properties,
            'settings': self._settings
        }


class Settings(Hashable):

    def __init__(
            self, refresh_interval: str = '1s', number_of_shards: int = 1,
            number_of_replicas: int = 1, max_result_window: int = 10000,
            **kws
    ):
        self.refresh_interval = refresh_interval
        self.number_of_shards = number_of_shards
        self.number_of_replicas = number_of_replicas
        self.max_result_window = max_result_window


class Index(Serializable):
    """Индекс ES."""

    basic_index_settings = {
        'refresh_interval', 'number_of_shards', 'number_of_replicas',
        'max_result_window'
    }
    allowed_index_settings = basic_index_settings | {'analysis'}

    def __init__(
            self, name: str, mappings: Union[dict, Mapping], settings: dict = None,
            aliases: dict = None, metadata: Metadata = None,
            text_search_fields: Collection = None, primary_key: str = 'id', **meta):
        """
        :param name: имя индекса
        :param settings: прочие настройки индекса в формате ES
        :param aliases: список ссылок на этот индекс
        :param metadata: объект `Metadata` для получения общих настроек и для
            регистрации индекса
        :param text_search_fields: поля, по которым осуществляется текстовый поиск
        :param primary_key: primary field name (used in bulk requests)
        """

        self._primary_key = primary_key

        _meta = {
            'text_search_fields': text_search_fields,
            'primary_key': primary_key,
            **meta
        }

        self._name = name
        self._aliases = aliases if aliases else {}

        if isinstance(mappings, dict):
            self.mapping = Mapping(index=self, **mappings)
        else:
            self.mapping = mappings
            self.mapping._index = proxy(self)

        self.mapping._meta.update(_meta)

        if settings:
            settings.update(settings.get('index', {}))
            self.settings = Settings(**settings)
            self.analysis = settings.get('analysis')
        else:
            self.settings = Settings()
            self.analysis = None

        _search_fields, _kw_fields = [], []

        for field in self.mapping.fields.values():
            if field.type == 'keyword':
                _kw_fields.append(field.name)
            elif field.type == 'text':
                _search_fields.append(field.name)

        self._text_search_fields = frozenset(_search_fields)
        self._kw_search_fields = frozenset(_kw_fields)
        self._search_fields = frozenset(self._text_search_fields | self._kw_search_fields)

        self._default_text_search_fields = []
        self._default_kw_search_fields = []

        if text_search_fields:
            text_search_fields = set(text_search_fields)
            for field in text_search_fields:
                field = self.mapping.fields[field]
                if field.name not in self._search_fields:
                    raise KeyError('"%s" — no such field or it is not searchable.' % field)
                elif field.type == 'keyword':
                    self._default_kw_search_fields.append(field.name)
                elif field.type == 'text':
                    self._default_text_search_fields.append(field.name)
        else:
            text_search_fields = [
                field for field in self._text_search_fields
                if self.mapping.fields[field].type == 'text'
                   and self.mapping.fields[field].settings.get('index', True)
                   and self.mapping.fields[field].settings.get('enabled', True)
            ]

        self._default_text_search_fields = tuple(text_search_fields)
        self._default_kw_search_fields = tuple(self._default_kw_search_fields)

        super().__init__()

        if metadata:
            metadata.register(self)
            if isinstance(metadata, ProxyType):
                self._metadata = metadata
            else:
                self._metadata = proxy(metadata)
        else:
            self._metadata = None

    @property
    def alias(self) -> str:
        return next(iter(self._aliases), None)

    @property
    def name(self):
        return self._name

    @property
    def text_search(self):
        return bool(self._search_fields)

    @property
    def max_result_window(self) -> int:
        return self.settings.get('index', {}).get('max_result_window', 10000)

    @property
    def primary_field(self) -> Field:
        return self.mapping.fields[self._primary_key]

    @property
    def primary_key(self) -> str:
        return self._primary_key

    def __call__(self, data: dict):
        """Нормализует поля документа в соответствии с мэппингом."""

        return self.mapping(data)

    def __str__(self):
        return self._name

    def __rtruediv__(self, other):
        """Строит URI до индекса."""

        return f'{other}/{self}'

    def __truediv__(self, other):
        """Строит URI до индекса."""

        return f'{self}/{other}'

    def repr(self):
        """Репрезентация индекса в формате ES."""

        settings = self.settings.repr()
        if self.analysis:
            settings['analysis'] = self.analysis

        return {
            'aliases': self._aliases,
            'mappings': self.mapping.repr(),
            'settings': settings
        }

    def filter(self, **kws) -> list:

        query = []

        for key, value in kws.items():
            if key in self:
                field_type = self[key].type
            else:
                field_type = 'keyword'
            if isinstance(value, dict):
                if 'exists' in value:
                    q = {'exists': {'field': key}}
                elif 'wildcard' in value:
                    q = {
                        "wildcard": {
                            key: {
                                "value": str(value['wildcard'])
                            }
                        }
                    }
                else:
                    q = {'range': {key: value}}
            elif isinstance(value, Sized) and not isinstance(value, str):
                if len(value) == 2 and field_type in Field.ranged_types:
                    _gte, _lte = value
                    q = {'range': {key: {'gte': _gte, 'lte': _lte}}}

                else:
                    q = {'terms': {key: value}}
            else:
                if field_type == 'text':
                    q = {'match_phrase_prefix': {key: value}}
                else:
                    q = {'term': {key: value}}
            query.append(q)

        return query

    def sort(self, *keys: Union[str, dict]) -> list:
        sorting = []
        for key in keys:
            sorting.append(key)
        return sorting

    def aggregate(self, *aggs: str, size=10) -> dict:
        query = {}
        for key in aggs:
            field_type = self.mapping.fields[key].type
            if field_type in Field.ranged_types:
                query[f'{key}_min'] = {'min': {'field': key}}
                query[f'{key}_max'] = {'max': {'field': key}}
            else:
                query[key] = {'terms': {'field': key, "size": size}}
        return query

    def highlight(
            self, fragment_size: int = 256, number_of_fragments: int = 1,
            order: str = "score", text_search_fields: List[str] = None) -> dict:

        if not self._text_search_fields:
            raise ValueError('Text search is disabled for this index.')

        if text_search_fields:
            text_search_fields = set(text_search_fields)
            text_search_fields = list(text_search_fields & self._text_search_fields)
        else:
            text_search_fields = self._text_search_fields

        _q = {
            "fragment_size": fragment_size,
            "number_of_fragments": number_of_fragments,
            "order": order
        }

        query = {
            'fields': {
                field: _q
                for field in text_search_fields
            }
        }

        return query

    def search(
            self, q: str, fuzziness: Union[int, str] = "AUTO", prefix_length: int = 1,
            text_search_fields: List[str] = None, operator: str = 'and') -> Optional[dict]:

        if not self._search_fields:
            return

        if text_search_fields:
            text_search_fields = set(text_search_fields)
            text_search_fields = list(text_search_fields & self._text_search_fields)
        else:
            text_search_fields = self._default_text_search_fields

        if not text_search_fields:
            return

        query = []
        match_query = {
            'query': q,
            'operator': operator
        }
        if fuzziness:
            match_query['fuzziness'] = fuzziness
        if prefix_length is not None:
            match_query['prefix_length'] = prefix_length

        if len(text_search_fields) > 1:
            match_query['fields'] = _fields = list(text_search_fields)
            prefix_q = {
                'query': q,
                'type': 'bool_prefix',
                'operator': operator,
                'fields': list(_fields),
                'boost': 5.0
            }
            query.append({'multi_match': prefix_q})
            query.append({'multi_match': match_query})
        else:
            field = next(iter(text_search_fields))
            query.append({'match_phrase_prefix': {field: q}})
            query.append({'match': {field: match_query}})

        return {'should': query, 'minimum_should_match': 1}
