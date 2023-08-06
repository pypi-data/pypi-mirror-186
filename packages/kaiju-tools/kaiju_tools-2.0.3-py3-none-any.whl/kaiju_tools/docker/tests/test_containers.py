from .fixtures import *


@pytest.mark.docker
def test_docker_container_ctx(sample_container):
    with sample_container as container:
        assert container._image.exists
        assert container.exists
    assert not container.exists
    assert not container._image.exists


@pytest.mark.docker
@pytest.mark.asyncio
async def test_docker_container_async_ctx(loop, sample_container):
    async with sample_container as container:
        assert container._image.exists
        assert container.exists
    assert not container.exists
    assert not container._image.exists
