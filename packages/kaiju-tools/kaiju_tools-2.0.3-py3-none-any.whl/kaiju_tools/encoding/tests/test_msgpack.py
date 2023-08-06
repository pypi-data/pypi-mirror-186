import datetime
import decimal
import sys
import uuid

import pytest
import tabulate

from ...serialization import Comparable
from ..json import dumps as json_dumps
from ..json import loads as json_loads
from ..msgpack import dumps, loads, msgpack_types, MsgpackType
from .fixtures import *


@pytest.mark.unit
def test_msgpack_packing_efficiency(serializable_data, logger):
    data = serializable_data
    headers = [
        'data type', 'msgpack size (bytes)', 'json size (bytes)', 'compression (%)'
    ]
    table = []

    for data_type, data in data.items():
        msg = dumps(data)
        json_msg = json_dumps(data)
        logger.debug('%s %s %s', data_type, msg, json_msg)
        msg_size = len(msg)
        json_size = len(json_msg.encode('utf-8'))
        ratio = round(json_size * 100 / msg_size)
        table.append([data_type, msg_size, json_size, ratio])

    print('\n\n')
    print(tabulate.tabulate(table, headers=headers))


@pytest.mark.unit
def test_msgpack_ext_types(logger):

    class SomeClass(Comparable, MsgpackType):

        ext_class_id = 42

        def __init__(self, x: int, y: str = None, z: str = None):
            self.x = x
            self.y = y
            self.z = z

    msgpack_types.register_class(SomeClass)

    data = SomeClass(x=1, z='test')
    logger.debug(data)
    msg = dumps(data)
    logger.debug(msg)
    new_data = loads(msg)
    logger.debug(new_data)
    assert data == new_data


@pytest.mark.unit
def test_msgpack_default_types(logger):

    data = {
        'text': 'text',
        'id': uuid.uuid4(),
        'set': frozenset({'a', 'b', 'c'}),
        'date': datetime.datetime.now(),
        'dec': decimal.Decimal('42.1')
    }

    logger.debug(data)
    msg = dumps(data)
    logger.debug(msg)
    new_data = loads(msg)
    logger.debug(new_data)
    data['date'] = data['date'].replace(microsecond=0)
    assert data == new_data
    assert new_data['dec'] == decimal.Decimal('42.1')
