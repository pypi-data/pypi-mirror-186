from exapi import Subject
from exapi.bitget.v1 import BaseWebSocket
from exapi.bitget.v1.constants import MIX_WS_URL
from exapi.bitget.v1.models import Topic


class MixWebSocket(BaseWebSocket):

    def __init__(self, url: str = MIX_WS_URL, **kwargs):
        super().__init__(url=url, **kwargs)

    async def ticker_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#tickers-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='ticker',
                inst_id=symbol,
                inst_type='mc',
            ),
        )

    async def candlesticks_stream(self, symbol: str, channel: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#candlesticks-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel=channel,
                inst_id=symbol,
                inst_type='mc',
            ),
        )

    async def depth_stream(self, symbol: str, depth: int = 5) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#order-book-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel=f'books{depth}',
                inst_id=symbol,
                inst_type='mc',
            ),
        )

    async def trades_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#trades-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='trade',
                inst_id=symbol,
                inst_type='mc',
            ),
        )

    async def new_trades_stream(self, symbol: str) -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#new-trades-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='tradeNew',
                inst_id=symbol,
                inst_type='mc',
            ),
        )

    async def account_stream(self, inst_type: str = 'UMCBL') -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#account-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='account',
                inst_id='default',
                inst_type=inst_type,
            ),
        )

    async def positions_stream(self, inst_type: str = 'UMCBL') -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#positions-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='positions',
                inst_id='default',
                inst_type=inst_type,
            ),
        )

    async def orders_stream(self, inst_type: str = 'UMCBL') -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#order-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='orders',
                inst_id='default',
                inst_type=inst_type,
            ),
        )

    async def plans_stream(self, inst_type: str = 'UMCBL') -> Subject:
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#plan-order-channel
        """
        return await self.subscribe(
            topic=Topic(
                channel='ordersAlgo',
                inst_id='default',
                inst_type=inst_type,
            ),
        )
