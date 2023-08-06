import pytest

from ..serializers import serializers
from .fixtures import *


@pytest.mark.unit
def test_serializers(serializable_data, logger):
    s = serializers['application/json'].dumps(serializable_data)
    logger.debug(s)
    _msg = serializers['application/json'].loads(s)
    logger.debug(_msg)
    assert serializable_data == _msg
