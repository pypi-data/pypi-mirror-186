from .fixtures import *


@pytest.mark.docker
def test_docker_image_ctx(sample_image):
    with sample_image as img:
        assert img.exists
    assert not img.exists


@pytest.mark.docker
@pytest.mark.asyncio
async def test_docker_image_async_ctx(loop, sample_image):
    async with sample_image as img:
        assert img.exists
    assert not img.exists
