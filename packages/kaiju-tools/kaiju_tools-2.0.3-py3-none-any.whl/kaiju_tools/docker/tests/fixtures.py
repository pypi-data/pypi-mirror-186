"""
Various test fixtures.

You can use `docker_container` and `per_session_docker_container` to implement your own container
fixtures for unit tests. See `DockerContainer` class for arguments description.

You also can use `docker_stack` and `per_session_docker_stack` for your custom docker-compose stacks
fixtures. See `DockerStack` class for arguments description.
"""

import uuid

import pytest

from kaiju_tools.tests.fixtures import *
from ..services import *


@pytest.fixture
def sample_dockerfile():
    return """
    FROM alpine:latest
    CMD echo test
    """


@pytest.fixture
def sample_compose_file():
    return """
    version: '3.9'
    services:
      pytest_test_service:
        image: "alpine:latest"
    """


@pytest.fixture
def sample_image(sample_dockerfile, application, logger):
    tag = str(uuid.uuid4())
    return DockerImage.from_string(
        sample_dockerfile, tag=tag, remove_on_exit=True, always_build=True, pull=True,
        app=application(), logger=logger)


@pytest.fixture
def sample_container(sample_dockerfile, application, logger):
    return DockerContainer(
        image={
            'dockerfile_str': sample_dockerfile,
            'tag': str(uuid.uuid4()),
            'remove_on_exit': True,
            'always_build': True,
            'pull': False,
        },
        name='pytest-sample-container',
        remove_on_exit=True,
        app=application(),
        logger=logger
    )


@pytest.fixture
def sample_stack(sample_compose_file, application, logger):
    return DockerStack.from_string(sample_compose_file, name=None, app=application(), logger=logger)
