import logging
import time

from anyio import sleep
from pydantic import BaseModel

from exapi import Subject, WebSocket
from exapi.bybit import utils
from exapi.bybit.exceptions import BybitException
from exapi.bybit.v3.enums import Operation
from exapi.bybit.v3.models import Message

logger = logging.getLogger(__name__)


def encode_message(message: BaseModel) -> str:
    return message.json(exclude_none=True, by_alias=True)


class BaseWebSocket(WebSocket):

    def __init__(
            self,
            url: str,
            api_key=None,
            api_secret=None,
            encoder=encode_message,
            **kwargs
    ):
        super().__init__(url=url, encoder=encoder, **kwargs)
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__subjects: dict[str, Subject] = dict()

    async def aclose(self) -> None:
        await self.unsubscribe_all()
        await sleep(3)
        await super().aclose()

    async def subscribe(self, topic: str) -> Subject:
        if not self.__subjects.get(topic):
            self.__subjects[topic] = Subject()
            await self.send(Operation.SUBSCRIBE, topic)

        return self.__subjects.get(topic)

    async def unsubscribe(self, topic: str) -> None:
        subject = self.__subjects.pop(topic, None)
        if isinstance(subject, Subject):
            subject.complete()
            await self.send(Operation.UNSUBSCRIBE, topic)

    async def unsubscribe_all(self) -> None:
        topics = list()

        while len(self.__subjects.keys()) > 0:
            topic, subject = self.__subjects.popitem()
            topics.append(topic)
            if isinstance(subject, Subject):
                subject.complete()

        if len(topics) > 0:
            logger.debug(f'Unsubscribe from all ({len(topics)} topics)')
            await self.send(Operation.UNSUBSCRIBE, *topics)

    async def __resubscribe_all(self) -> None:
        topics = list(self.__subjects.keys())
        if len(topics) > 0:
            logger.debug(f'Resubscribe to all ({len(topics)} topics)')
            await self.send(Operation.SUBSCRIBE, *topics)

    async def _on_message(self, message):
        if not isinstance(message, dict):
            return

        topic = message.get('topic')

        if not topic:
            return

        subject = self.__subjects.get(topic)

        if not subject:
            return

        subject.next(message)

    async def _auth(self):
        # Generate expires.
        expires = int((time.time() + 10) * 1000)
        payload = f"GET/realtime{expires}"
        sign = utils.sign(payload=payload, secret=self.__api_secret)

        await self.send(
            Operation.AUTH,
            self.__api_key,
            expires,
            sign,
        )

        message = self._decoder(await self._socket.recv())

        ret_msg = message.get('ret_msg')
        ret_code = message.get('ret_code')

        if len(ret_msg):
            raise BybitException(f'Error: code={ret_code}, msg="{ret_msg}"', code=ret_code)

        assert message.get('op') == Operation.AUTH.value
        assert message.get('success') is True

    async def _on_connect(self):
        if self.__api_key and self.__api_secret:
            await self._auth()
        await self.__resubscribe_all()

    async def send(self, op: Operation, *args):
        logger.debug(f'Send: op={op.value}, {args=}')
        await self.send_message(message=Message(op=op, args=args))
