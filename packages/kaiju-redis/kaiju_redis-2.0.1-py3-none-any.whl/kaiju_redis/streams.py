from traceback import print_exc
from typing import Optional

from kaiju_tools.streams import Consumer, Producer, Listener
from kaiju_tools.functions import retry

from .transport import RedisTransportService

__all__ = ['RedisConsumer', 'RedisProducer', 'RedisListener']


class RedisConsumer(Consumer):
    """Stream consumer."""

    record_trim_size = 100000
    timeout_ms = 500
    max_records = 10
    pending_messages_idle_time = 60
    _transport: RedisTransportService

    def __init__(
        self,
        *args,
        group_id: str = None,
        record_trim_size=record_trim_size,
        timeout_ms: int = timeout_ms,
        max_records: int = max_records,
        pending_messages_idle_time: int = pending_messages_idle_time,
        **kws,
    ):
        """Initialize.

        :param args:
        :param group_id:
        :param record_trim_size:
        :param timeout_ms:
        :param max_records:
        :param pending_messages_idle_time:
        :param kws:
        """
        super().__init__(*args, **kws)
        self.consumer_id = str(self.app.id)
        self.group_id = group_id if group_id else self.app.name
        self.record_trim_size = max(1, int(record_trim_size))
        self.timeout_ms = max(1, int(timeout_ms))
        self.max_records = max(1, int(max_records))
        self.pending_messages_idle_time = max(1, int(pending_messages_idle_time))

    async def _init(self):
        pass

    async def _close(self):
        pass

    async def process_pending_messages(self):
        await self._unlocked.wait()
        try:
            pending = await self._transport.xpending(
                self.topic, self.group_id, idle=self.pending_messages_idle_time * 1000
            )
            if pending:
                message_ids = [row[0] for row in pending]
                self._ready.clear()
                batch = await self._transport.xreadgroup(
                    self.group_id, self.consumer_id, streams={self.topic: message_ids}
                )
                await self._process_batch(batch)
        except Exception as exc:
            if self.app.debug:
                print_exc()
            self.logger.error(
                'There was an exception processing pending messages. [%s]: %s', exc.__class__.__name__, exc
            )

    async def _get_message_batch(self):
        batch = await self._transport.xreadgroup(
            self.group_id,
            self.consumer_id,
            count=self.max_records,
            block=self.timeout_ms,
            streams={self.topic: '>'},
            noack=True,
        )
        return batch

    async def _process_batch(self, batch):

        acks = []

        if not batch:
            return

        for topic, rows in batch.items():
            for row in rows:
                row_id, data = row
                headers, body = data[b'h'], data[b'b']
                if body:
                    headers = self._serializer.loads(headers) if headers else None
                    await self._process_request(headers, body)
                acks.append(row_id)

        if acks:
            await retry(
                self._transport.xack,
                args=(self.topic, self.group_id),
                kws={'identifiers': acks},
                retries=10,
                retry_timeout=1.0,
                logger=self.logger,
            )

    async def trim_records(self):
        await self._transport.xtrim(
            self.topic, trim_strategy=b'MAXLEN', threshold=self.record_trim_size, trim_operator=b'~'
        )


class RedisProducer(Producer):
    """Stream message producer class."""

    _transport: RedisTransportService

    async def _init(self):
        pass

    async def _close(self):
        pass

    async def _send_request(self, topic: str, key: Optional, headers: dict, request: bytes, **_):
        if not key:
            key = '*'
        if headers:
            headers = self._serializer.dumps_bytes(headers)
        else:
            headers = ''
        resp = await self._transport.xadd(topic, {'h': headers, 'b': request}, identifier=key)
        self.logger.debug('New record: [%s] %s', topic, resp)


class RedisListener(Listener):
    """Stream listener (manages producers and consumers)."""

    service_name = 'streams.redis'
    consumer_class = RedisConsumer
    producer_class = RedisProducer
    transport_class = RedisTransportService

    async def _init(self):
        group_id = self._consumer_settings.get('group_id')
        for topic in self.topics:
            topic = self.consumer_class.get_topic_key(self.app.env, self.namespace, topic)
            if group_id:
                self.logger.debug('Checking group "%s" for topic "%s".', group_id, topic)
                groups = await self._transport.xinfo_groups(topic)
                group_names = frozenset(g[b'name'].decode() for g in groups)
                self.logger.debug('Groups for topic "%s": "%s".', topic, group_names)
                if group_id not in group_names:
                    self.logger.debug('Adding a new group "%s" to topic "%s".', group_id, topic)
                    await self._transport.xgroup_create(topic, group_id, identifier='$', mkstream=True)

    async def _daemon_task(self):
        for consumer in self._consumers.values():
            if not consumer.closed:
                await consumer.trim_records()
                # await consumer.process_pending_messages()
