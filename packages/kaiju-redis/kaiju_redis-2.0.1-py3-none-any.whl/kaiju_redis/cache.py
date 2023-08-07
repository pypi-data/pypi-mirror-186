import textwrap
from typing import Awaitable

from kaiju_tools.cache import BaseCacheService

from .transport import RedisTransportService

__all__ = ['RedisCacheService']


class RedisCacheService(BaseCacheService):
    """Provides caching via Redis or KeyDB."""

    M_SET_EXP_SCRIPT = """
    local ttl = ARGV[1]
    for i, key in pairs(KEYS) do
        redis.call('SETEX', key, ttl, ARGV[i + 1])
    end
    """

    M_EXISTS_SCRIPT = """
    local result = {}
    for i, key in pairs(KEYS) do
        result[i] = redis.call('EXISTS', key)
    end
    return result
    """

    transport_cls = RedisTransportService
    _m_set_exp_script = None  #: compiled script
    _m_exists_script = None  #: compiled script
    _transport: RedisTransportService = None

    async def init(self):
        await super().init()
        self._m_set_exp_script = self._transport.register_script(textwrap.dedent(self.M_SET_EXP_SCRIPT))
        self._m_exists_script = self._transport.register_script(textwrap.dedent(self.M_EXISTS_SCRIPT))

    def _exists(self, key: str) -> Awaitable:
        return self._transport.exists([key])

    def _m_exists(self, *keys: str) -> Awaitable:
        return self._m_exists_script.execute(keys=keys)

    def _get(self, key: str) -> Awaitable:
        return self._transport.get(key)

    def _m_get(self, *keys: str) -> Awaitable:
        return self._transport.mget(keys)

    def _set(self, key: str, value, ttl: int) -> Awaitable:
        if ttl:
            return self._transport.setex(key, value, ttl)
        else:
            return self._transport.set(key, value)

    def _m_set(self, keys: dict, ttl: int) -> Awaitable:
        if ttl:
            return self._m_set_exp_script.execute(keys=list(keys.keys()), args=[ttl, *list(keys.values())])
        else:
            return self._transport.mset(keys)

    def _delete(self, key: str) -> Awaitable:
        return self._transport.delete([key])

    async def _m_delete(self, *keys: str):
        self.logger.info('DELETE')
        try:
            await self._transport.delete(keys)
        except Exception as exc:
            self.logger.info(str(exc))
        self.logger.info('OK')
