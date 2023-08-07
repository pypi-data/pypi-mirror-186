"""Place your pytest fixtures here."""

import pytest

from kaiju_tools.streams.etc import Topics
from kaiju_tools.docker import DockerContainer
from kaiju_tools.tests.fixtures import *
from kaiju_tools.rpc.tests.fixtures import *

from ..services import *

REDIS_PORT = 6399


def _redis_container(logger):
    return DockerContainer(
        image={'tag': 'eqalpha/keydb', 'version': 'latest'},
        name='pytest-redis',
        ports={'6379': str(REDIS_PORT)},
        healthcheck={
            'test': "echo 'INFO' | keydb-cli",
            'interval': 100000000,
            'timeout': 3000000000,
            'start_period': 1000000000,
            'retries': 3,
        },
        sleep_interval=0.5,
        remove_on_exit=True,
        logger=logger,
    )


@pytest.fixture
def redis(logger):
    """Return a new redis container. See `kaiju_tools.tests.fixtures.container` for more info."""
    with _redis_container(logger) as c:
        yield c


@pytest.fixture(scope='session')
def per_session_redis(logger):
    """Return a new redis container. See `kaiju_tools.tests.fixtures.container` for more info."""
    with _redis_container(logger) as c:
        yield c


@pytest.fixture
def redis_transport(application, logger):
    """Get transport class."""
    return RedisTransportService(app=application(), host='localhost', port=REDIS_PORT, logger=logger)


@pytest.fixture
def redis_cache(redis_transport, logger):
    """Get cache class."""
    return RedisCacheService(app=redis_transport.app, transport=redis_transport, logger=logger)


@pytest.fixture
def redis_locks(redis_transport, logger):
    """Get locks class."""
    return RedisLocksService(app=redis_transport.app, transport=redis_transport, logger=logger)


@pytest.fixture
def redis_listener(redis_transport, redis_locks, rpc_interface, logger):
    """Get stream listener class."""
    return RedisListener(
        app=redis_transport.app,
        topics=[Topics.rpc, Topics.callback],
        transport=redis_transport,
        rpc_service=rpc_interface,
        locks_service=redis_locks,
        consumer_settings={'group_id': 'pytest', 'timeout_ms': 100},
        logger=logger,
    )
