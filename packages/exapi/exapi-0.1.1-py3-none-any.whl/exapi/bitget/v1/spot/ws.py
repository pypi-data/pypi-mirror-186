from exapi import Subject
from exapi.bitget.v1 import BaseWebSocket
from exapi.bitget.v1.constants import SPOT_WS_URL
from exapi.bitget.v1.models import Topic


class SpotWebSocket(BaseWebSocket):

    def __init__(self, url: str = SPOT_WS_URL, **kwargs):
        super().__init__(url=url, **kwargs)

    async def ticker_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#tickers-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='sp',
                channel='ticker',
                inst_id=symbol,
            ),
        )

    async def candlesticks_stream(self, symbol: str, channel: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#candlesticks-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='sp',
                channel=channel,
                inst_id=symbol,
            ),
        )

    async def depth_stream(self, symbol: str, depth: int = 5) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#depth-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='sp',
                channel=f'books{depth}',
                inst_id=symbol,
            ),
        )

    async def trades_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#trades-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='sp',
                channel='trade',
                inst_id=symbol,
            ),
        )

    async def account_stream(self) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#account-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='spbl',
                channel='account',
                inst_id='default',
            ),
        )

    async def orders_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/spot/#order-channel
        """
        return await self.subscribe(
            topic=Topic(
                inst_type='spbl',
                channel='orders',
                inst_id=symbol,
            ),
        )
