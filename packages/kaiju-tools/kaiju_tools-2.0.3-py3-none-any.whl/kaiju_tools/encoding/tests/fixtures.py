import datetime
import uuid

import pytest


@pytest.fixture
def serializable_data():
    data = {
        'int': 42,
        'str': 'some text',
        'unicode': 'уникоде',
        'bool': True,
        'uuid': uuid.uuid4(),
        'list': ['some', 'text', 42],
        'time': datetime.datetime.now()
    }
    return data
