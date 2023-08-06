import asyncio
import json
import logging
import typing

from websockets.legacy.client import WebSocketClientProtocol, connect

from exapi.types import Dencoder, Encoder

logger = logging.getLogger(__name__)


class WebSocket:

    def __init__(
            self,
            url: str,
            encoder: Encoder = json.dumps,
            decoder: Dencoder = json.loads,
    ):
        self._url = url
        self._encoder = encoder
        self._decoder = decoder
        self._socket: WebSocketClientProtocol | None = None
        self._auto_reconnect = True
        self._is_connected = False

    async def aclose(self) -> None:
        self._auto_reconnect = False
        logger.info(f'Disconecting from {self._url}')
        if self._socket is not None:
            await self._socket.close()
        self._socket = None
        self._is_connected = False
        logger.info(f'Disconected from {self._url}')

    async def _on_connect(self) -> None:
        print(f'on_connect: {self._url}')

    async def _on_message(self, message) -> None:
        print(f'on_message: {message}')

    async def _listen_messages(self) -> None:
        async for message in self._socket:
            try:
                await self._on_message(message=self._decoder(message))
            except Exception:
                logger.exception(f'Unexpected listen messages exception')

    async def forever(self, **kwargs) -> None:
        logger.info(f'Connecting to {self._url}')
        self._auto_reconnect = True
        async for socket in connect(self._url, **kwargs):
            logger.info(f'Connected to {self._url}')
            self._socket = socket
            await self._on_connect()
            self._is_connected = True
            await self._listen_messages()
            self._is_connected = False
            self._socket = None
            if not self._auto_reconnect:
                break

    async def wait_connected(self) -> None:
        while not self._is_connected:
            await asyncio.sleep(0.1)

    async def send_message(self, message) -> None:
        await self._socket.send(message=self._encoder(message))

    async def __aenter__(self) -> typing.Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.aclose()
