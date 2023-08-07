import pytest

from kaiju_tools.streams.tests.test_streams import stream_test_function

from .fixtures import *


@pytest.mark.asyncio
async def test_redis_listener(redis, redis_listener, logger):
    await stream_test_function(redis_listener, logger)
