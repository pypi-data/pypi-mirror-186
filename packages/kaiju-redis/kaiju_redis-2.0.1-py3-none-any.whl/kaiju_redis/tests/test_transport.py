import pytest

from .fixtures import *


@pytest.mark.asyncio
async def test_redis_transport(redis, redis_transport, logger):
    log = await redis_transport.info()
    logger.debug(log)
