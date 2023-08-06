from exapi import Subject
from exapi.bybit.v3 import BaseWebSocket


class PublicWebSocket(BaseWebSocket):

    async def depth_stream(self, symbol: str, depth: int = 40) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websocketdepth
        """
        return await self.subscribe(
            topic=f'orderbook.{depth}.{symbol}',
        )

    async def trade_stream(self, symbol: str) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websockettrade
        """
        return await self.subscribe(
            topic=f'trade.{symbol}',
        )

    async def kline_stream(self, symbol: str, interval: str = "1h") -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websocketkline
        """
        return await self.subscribe(
            topic=f'kline.{interval}.{symbol}',
        )

    async def tickers_stream(self, symbol: str) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websockettickers
        """
        return await self.subscribe(
            topic=f'tickers.{symbol}',
        )

    async def bookticker_stream(self, symbol: str) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websocektbookticker
        """
        return await self.subscribe(
            topic=f'bookticker.{symbol}',
        )
