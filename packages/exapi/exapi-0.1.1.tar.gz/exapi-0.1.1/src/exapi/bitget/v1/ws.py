import logging
import time

import anyio

from exapi import WebSocket
from exapi import Subject
from exapi.bitget import utils
from exapi.bitget.exceptions import BitgetException
from exapi.bitget.v1.constants import REQUEST_PATH
from exapi.bitget.v1.enums import Operation
from exapi.bitget.v1.models import Action, BaseModel, Event, Login, Message, Topic

logger = logging.getLogger(__name__)


def encode_message(message: BaseModel) -> str:
    return message.json(exclude_none=True, by_alias=True)


class BaseWebSocket(WebSocket):

    def __init__(
            self,
            url: str,
            api_key=None,
            api_secret=None,
            api_passphrase=None,
            encoder=encode_message,
            **kwargs
    ):
        super().__init__(url=url, encoder=encoder, **kwargs)
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__api_passphrase = api_passphrase
        self.__subjects: dict[Topic, Subject] = dict()

    async def aclose(self) -> None:
        await self.unsubscribe_all()
        await anyio.sleep(3)
        await super().aclose()

    async def subscribe(self, topic: Topic) -> Subject:
        if not self.__subjects.get(topic):
            self.__subjects[topic] = Subject()
            await self.send(Operation.SUBSCRIBE, topic)

        return self.__subjects.get(topic)

    async def unsubscribe(self, topic: Topic) -> None:
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

    @staticmethod
    async def _process_event(event: Event) -> None:
        if event.code != 0:
            return logger.error(f'WebSocket error code={event.code}, msg="{event.msg}"')
        logger.debug(f'Process event: {event!r}')

    async def _process_action(self, action: Action) -> None:
        subject = self.__subjects.get(action.topic)

        if not subject:
            return

        subject.next(action)

    async def _on_message(self, message):
        if 'event' in message:
            return await self._process_event(event=Event(**message))
        if 'data' in message:
            return await self._process_action(action=Action(**message))

    async def _auth(self):
        timestamp = int(time.time())
        payload = utils.calc_hash(timestamp=timestamp, method='GET', request_path=REQUEST_PATH)
        sign = utils.sign(payload=payload, secret=self.__api_secret)

        await self.send(
            Operation.LOGIN,
            Login(
                api_key=self.__api_key,
                passphrase=self.__api_passphrase,
                timestamp=timestamp,
                sign=sign,
            ),
        )

        message = self._decoder(await self._socket.recv())
        event = Event(**message)

        if event.code != 0:
            raise BitgetException(f'Error: code={event.code}, msg="{event.msg}"', code=event.code)

        assert event.event == 'login'

    async def _on_connect(self):
        if self.__api_key and self.__api_secret and self.__api_passphrase:
            await self._auth()
        await self.__resubscribe_all()

    async def send(self, op: Operation, *args):
        logger.debug(f'Send: op={op.value}, {args=}')
        await self.send_message(message=Message(op=op, args=args))
