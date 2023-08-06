from .fixtures import *


@pytest.mark.docker
def test_docker_stack_ctx(sample_stack):
    with sample_stack as stack:
        assert stack.exists
    assert not stack.exists


@pytest.mark.docker
@pytest.mark.asyncio
async def test_docker_stack_async_ctx(loop, sample_stack):
    async with sample_stack as stack:
        assert stack.exists
    assert not stack.exists
