import pytest

from kaiju_tools.cache.tests.test_cache import cache_service_test

from .fixtures import *


@pytest.mark.asyncio
async def test_redis_cache(redis, redis_cache, logger):
    await cache_service_test(redis_cache, logger)
