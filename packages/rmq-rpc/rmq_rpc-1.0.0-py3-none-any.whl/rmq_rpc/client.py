import asyncio
import json
import logging
import pickle
import uuid
from functools import partial
from typing import Any, Callable, Dict, List, Union

from aio_pika import DeliveryMode, Message
from aio_pika.abc import (
    AbstractIncomingMessage,
    AbstractRobustChannel,
    AbstractRobustExchange,
    AbstractRobustQueue,
    ConsumerTag,
)

from .constant import CANCEL_QUEUE_NAME
from .enums import ContentType
from .serializers import BaseSerializer

log = logging.getLogger(__name__)


class Client:
    tmp_queue: AbstractRobustQueue = None
    tmp_consumer: ConsumerTag = None

    def __init__(
        self, channel: AbstractRobustChannel, exchange: AbstractRobustExchange
    ) -> None:
        self.loop = asyncio.get_event_loop()
        self.channel = channel
        self.exchange = exchange
        self.futures: Dict[str, asyncio.Future] = {}
        self.serializers: List[BaseSerializer] = []

    @classmethod
    async def create(
        cls, channel: AbstractRobustChannel, exchange: AbstractRobustExchange
    ):
        instance = cls(channel, exchange)
        tmp_queue = await channel.declare_queue(exclusive=True, auto_delete=True)
        await tmp_queue.bind(exchange)
        tmp_consumer = await tmp_queue.consume(
            instance.on_message_received, no_ack=True
        )
        instance.tmp_queue = tmp_queue
        instance.tmp_consumer = tmp_consumer
        return instance

    def add_serializer(self, serializer: BaseSerializer):
        self.serializers.append(serializer)

    async def on_message_received(self, msg: AbstractIncomingMessage):
        cid = msg.correlation_id
        if cid is None:
            log.warn("Get messages without a correlation ID")
            return

        future = self.futures.pop(cid, None)
        if future is None:
            log.warning("Unknown message: %r", msg)
            return

        message = None
        try:
            success, result = pickle.loads(msg.body)
            if not success:
                future.set_exception(result)
                return

            for serializer in self.serializers:
                match = msg.content_type in serializer.content_type
                if match:
                    message = await serializer.deserialize(result)
                    break

            if message is None:
                raise TypeError(
                    f"Message are not supported. Serializer is not available for {msg.content_type!r}"
                )
        except Exception as e:
            log.error("Failed to deserialize message")
            future.set_exception(e)
            return

        future.set_result(message)

    def create_future(self):
        future = self.loop.create_future()
        cid = str(uuid.uuid4())
        self.futures[cid] = future
        future.add_done_callback(partial(self._remove_future, cid))
        return cid, future

    def _remove_future(self, cid: str, f: asyncio.Future):
        log.debug("Removing future: " + cid)
        self.futures.pop(cid, None)

    async def call(
        self,
        func: Union[Callable, str],
        *,
        args: List[Any] = [],
        kwargs: Dict[str, Any] = {},
        timeout: float = None,
        **msg_kwargs,
    ):
        if callable(func):
            func = func.__name__

        if not isinstance(func, str):
            raise ValueError(
                "func parameter must be a string. (this is the same as the function name)"
            )

        params = {"args": args, "kwargs": kwargs}
        body = json.dumps(params).encode()
        cid, future = self.create_future()
        msg_kwargs.setdefault("content_type", ContentType.TEXT)
        msg_kwargs["correlation_id"] = cid
        msg_kwargs["delivery_mode"] = DeliveryMode.NOT_PERSISTENT
        msg_kwargs["reply_to"] = self.tmp_queue.name
        message = Message(body, **msg_kwargs)
        await self.exchange.publish(message, func)
        log.info(f"Message has been sent to: {func!r}")
        log.debug("Waiting for the result...")
        try:
            result = await asyncio.wait_for(future, timeout)
            log.debug(f"Get results from {func!r}: {result}")
        except asyncio.TimeoutError:
            msg = Message(b"", correlation_id=cid)
            await self.exchange.publish(msg, routing_key=CANCEL_QUEUE_NAME)
            log.debug(f"Cancel task: {cid!r}")
            raise

        return result

    async def close(self):
        if self.tmp_queue and self.tmp_consumer:
            await self.tmp_queue.cancel(self.tmp_consumer)
            await self.tmp_queue.delete(if_unused=False, if_empty=False)
