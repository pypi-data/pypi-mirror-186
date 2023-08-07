import pytest

from kaiju_tools.locks.tests.test_locks import locks_service_test

from .fixtures import *


@pytest.mark.asyncio
async def test_keydb_locks_service(redis, redis_locks, logger):
    await locks_service_test(redis, redis_locks, logger)
