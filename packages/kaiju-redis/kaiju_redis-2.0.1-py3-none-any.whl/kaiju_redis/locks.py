import textwrap

from coredis.exceptions import ResponseError

from kaiju_tools.locks import BaseLocksService, StatusCodes
from kaiju_tools.locks.exceptions import *

from .transport import RedisTransportService
from .cache import RedisCacheService

__all__ = ['RedisLocksService']


class RedisLocksService(BaseLocksService):
    """
    Locks service with Redis backend.

    :param app:
    :param transport: redis transport class
    :param args: see `BaseLocksService`
    :param kws: see `BaseLocksService`
    :param logger:
    """

    LOCK_SCRIPT = f"""
    local e = redis.call('get', KEYS[1])
    if not e then
        redis.call('set', KEYS[1], ARGV[1])
        redis.call('expire', KEYS[1], ARGV[2])
        return redis.status_reply('{StatusCodes.OK}')
    else
        return redis.error_reply('{StatusCodes.LOCK_EXISTS}')
    end"""

    UNLOCK_SCRIPT = f"""
    local _id = redis.call('get', KEYS[1])
    if _id == ARGV[1] then
        redis.call('del', KEYS[1])
        return redis.status_reply('{StatusCodes.OK}')
    elseif not _id then
        return redis.status_reply('{StatusCodes.OK}')
    else
        return redis.error_reply('{StatusCodes.NOT_LOCK_OWNER}')
    end"""

    RENEW_SCRIPT = """
    for i, key in pairs(KEYS) do
        redis.call('expire', key, ARGV[i])
    end
    """

    EXISTS_SCRIPT = RedisCacheService.M_EXISTS_SCRIPT
    transport_cls = RedisTransportService
    _lock_script = None
    _unlock_script = None
    _renew_script = None
    _exists_script = None

    async def init(self):
        await super().init()
        self._lock_script = self._transport.register_script(textwrap.dedent(self.LOCK_SCRIPT))
        self._unlock_script = self._transport.register_script(textwrap.dedent(self.UNLOCK_SCRIPT))
        self._renew_script = self._transport.register_script(textwrap.dedent(self.RENEW_SCRIPT))
        self._exists_script = self._transport.register_script(textwrap.dedent(self.EXISTS_SCRIPT))

    async def _check_exists(self, keys: list) -> frozenset:
        data = await self._exists_script.execute(keys=keys)
        if data:
            return frozenset(data)
        else:
            return frozenset()

    async def _acquire(self, keys: list, identifier: str, ttl: int):
        try:
            await self._lock_script.execute(keys=keys, args=[identifier, ttl])
        except ResponseError as exc:
            if str(exc) == StatusCodes.LOCK_EXISTS:
                exc = LockExistsError(
                    'One of the provided locks exists.',
                    code=StatusCodes.LOCK_EXISTS, keys=keys)
            raise exc

    async def _release(self, keys: list, identifier: str):
        try:
            await self._unlock_script.execute(keys=keys, args=[identifier])
        except ResponseError as exc:
            if str(exc) == StatusCodes.NOT_LOCK_OWNER:
                exc = NotALockOwnerError(
                    'The lock can\'t be released not by its owner.',
                    code=StatusCodes.NOT_LOCK_OWNER, keys=keys, identifier=identifier)
            raise exc

    async def _renew(self, keys: list, values: list):
        await self._renew_script.execute(keys=keys, args=values)

    async def _owner(self, key: str):
        owner = await self._transport.get(key)
        if owner:
            owner = owner.decode('utf-8')
            return owner
