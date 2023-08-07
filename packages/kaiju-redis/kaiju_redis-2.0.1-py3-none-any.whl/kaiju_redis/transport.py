from coredis import Redis, RedisCluster

from kaiju_tools.services import ContextableService

__all__ = ['RedisTransportService']


class RedisTransportService(ContextableService):
    """Redis transport."""

    transport_class = Redis
    cluster_transport_class = RedisCluster

    def __init__(
        self,
        app,
        *args,
        cluster: bool = False,
        connect_timeout: int = 30,
        max_idle_time: int = 60,
        retry_on_timeout=True,
        logger=None,
        **kws,
    ):
        """Initialize.

        :param app:
        :param args: additional transport cls args
        :param cluster: use cluster connector class
        :param connect_timeout: connection timeout
        :param max_idle_time: max connection idle time
        :param retry_on_timeout: retry connection on timeout
        :param logger:
        :param kws: additional transport cls args
        """
        ContextableService.__init__(self, app, logger=logger)
        if cluster:
            cls = self.cluster_transport_class
        else:
            cls = self.transport_class
        self._transport = cls(
            *args,
            connect_timeout=connect_timeout,
            max_idle_time=max_idle_time,
            retry_on_timeout=retry_on_timeout,
            **kws,
        )

    def __getattr__(self, item):
        return getattr(self._transport, item)

    async def init(self):
        self.connection_pool.reset()

    async def close(self):
        self.connection_pool.disconnect()
