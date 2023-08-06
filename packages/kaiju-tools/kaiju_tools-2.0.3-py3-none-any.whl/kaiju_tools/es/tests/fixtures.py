"""Elasticsearch client services test fixtures."""

from datetime import datetime
from random import randint, choice

import pytest

from ..schema import Index, Field
from ..service import ESService

__all__ = [
    'es_test_settings', 'es_test_index', 'es_document', 'es_service',
    'es_environment', 'ES_TEST_INDEX_SIZE'
]

ES_TEST_INDEX_SIZE = 500


@pytest.fixture(scope='session')
def es_test_settings() -> dict:
    """ES service settings for localhost."""

    return {
        'host': 'http://127.0.0.1:9200'
    }


@pytest.fixture
def es_document(random_string, random_date, tempest):
    """A ES compatible document fixture.

    > es_document(42) - will create a document dict with id=42

    """

    tags = ['a', 'b', 'c']
    t = datetime.now().date()

    def _es_document(id):
        return {
            'id': str(id),
            'title': random_string(16),
            'text': choice(tempest),
            'percent': randint(0, 100),
            'timestamp': random_date(),
            'tags': choice(tags),
            'active': bool(randint(0, 1)),
            'duration': {
                'gte': random_date(to_=t),
                'lte': random_date(from_=t)
            }
        }

    return _es_document


@pytest.fixture
def es_test_index(random_string) -> Index:
    """A test ES index schema that matches `es_doc` fixture."""

    name = random_string(8).lower()

    idx = Index(
        name,
        mappings={
            '_meta': {
                'class': 'Card',
                'description': 'Product info data storage.'
            },
            'dynamic': False,
            'properties': [
                Field('id', 'keyword', norms=False),
                Field('title', 'keyword', index=False),
                Field(
                    'text', 'text',
                    analyzer="standard", index_options="offsets",
                    index_prefixes={"min_chars": 3, "max_chars": 6},
                    index_phrases=True, ),
                Field('timestamp', 'date'),
                Field('duration', 'date_range'),
                Field('tags', 'keyword'),
                Field('percent', 'integer'),
                Field('active', 'boolean')
            ]
        },
        text_search_fields=['text'],
        settings={
            'index': {
                'number_of_shards': 1,
                'number_of_replicas': 1,
                'index.refresh_interval': '1s',
                'index.max_result_window': 10000
            }
        },
        primary_key='id',
        metadata=None
    )

    return idx


@pytest.fixture
async def es_service(es_test_settings, web_application, loop):
    """A ready to use ES service instance."""

    async with ESService(web_application, **es_test_settings) as es:
        yield es


@pytest.fixture
async def es_environment(es_service, es_document, es_test_index, loop):
    """Test environment.

    It inits a Elasticsearch service, creates an index and fills it with
    some sample data.

    :returns: a ready to use ES service and a test index schema
    """

    es_test_index = await es_service.init_index(es_test_index)
    docs = [es_document(n) for n in range(ES_TEST_INDEX_SIZE)]
    await es_service.insert(es_test_index, docs)
    del docs
    await es_service.refresh(es_test_index)
    yield es_service, es_test_index

    es_test_index = await es_service.init_index(es_test_index)
    await es_service.delete_index(es_test_index)
