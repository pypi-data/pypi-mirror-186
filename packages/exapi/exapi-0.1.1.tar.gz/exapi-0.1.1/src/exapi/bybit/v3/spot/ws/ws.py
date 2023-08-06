from typing import Self

from anyio import CancelScope, create_task_group, sleep

from exapi.bybit.v3.constants import SPOT_WS_PRIVATE_URL, SPOT_WS_PUBLIC_URL
from exapi.bybit.v3.spot.ws.private import PrivateWebSocket
from exapi.bybit.v3.spot.ws.public import PublicWebSocket
from src.exapi.subject import Subject


class SpotWebSocket:

    def __init__(
            self,
            api_key=None,
            api_secret=None,
    ):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__public_ws: PublicWebSocket | None = None
        self.__private_ws: PrivateWebSocket | None = None

    async def wait_connected(self) -> None:
        while not self.__public_ws or not self.__private_ws:
            await sleep(0.1)

    async def __forever_public_ws(self) -> None:
        async with PublicWebSocket(url=SPOT_WS_PUBLIC_URL) as ws:
            async with create_task_group() as task_group:
                task_group.start_soon(ws.forever)
                await ws.wait_connected()
                self.__public_ws = ws

    async def __forever_private_ws(self) -> None:
        async with PrivateWebSocket(
                url=SPOT_WS_PRIVATE_URL,
                api_key=self.__api_key,
                api_secret=self.__api_secret,
        ) as ws:
            async with create_task_group() as task_group:
                task_group.start_soon(ws.forever)
                await ws.wait_connected()
                self.__private_ws = ws

    async def forever(self) -> None:
        async with create_task_group() as task_group:
            task_group.start_soon(self.__forever_public_ws)
            task_group.start_soon(self.__forever_private_ws)
            await self.wait_connected()

    async def depth_stream(self, symbol: str, depth: int = 40) -> Subject:
        return await self.__public_ws.depth_stream(symbol=symbol, depth=depth)

    async def trade_stream(self, symbol: str) -> Subject:
        return await self.__public_ws.trade_stream(symbol=symbol)

    async def kline_stream(self, symbol: str, interval: str = "1h") -> Subject:
        return await self.__public_ws.kline_stream(symbol=symbol, interval=interval)

    async def tickers_stream(self, symbol: str) -> Subject:
        return await self.__public_ws.tickers_stream(symbol=symbol)

    async def bookticker_stream(self, symbol: str) -> Subject:
        return await self.__public_ws.bookticker_stream(symbol=symbol)

    async def outbound_account_info_stream(self) -> Subject:
        return await self.__private_ws.outbound_account_info_stream()

    async def order_stream(self) -> Subject:
        return await self.__private_ws.order_stream()

    async def stop_order_stream(self) -> Subject:
        return await self.__private_ws.stop_order_stream()

    async def ticket_info_stream(self) -> Subject:
        return await self.__private_ws.ticket_info_stream()

    async def aclose(self) -> None:
        async with create_task_group() as task_group:
            with CancelScope(shield=True):
                task_group.start_soon(self.__public_ws.aclose)
                task_group.start_soon(self.__private_ws.aclose)
                self.__public_ws = None
                self.__private_ws = None

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.aclose()
