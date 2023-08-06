import pytest

from ..logging import Loggable


@pytest.mark.unit
def test_loggable_class(logger):

    class C(Loggable):
        pass

    c = C(logger=logger)
    c.logger.info('testing...')
