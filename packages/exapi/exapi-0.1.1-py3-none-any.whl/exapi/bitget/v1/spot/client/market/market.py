from exapi.bitget.v1 import BaseClient
from exapi.bitget.v1.constants import SPOT_MARKET_PATH
from exapi.bitget.v1.spot.client.market.models import (
    CandlesParams,
    OrderBookParams,
    PublicTradeParams,
    TickerParams,
)
from exapi.bitget.v1.spot.enums import Interval, OrderBookType


class Market:

    async def fetch_ticker(
            self: 'BaseClient',
            symbol: str,
    ) -> dict:
        """
        Fetch ticker information according to the currency pair
        """
        return await self.get(
            url=SPOT_MARKET_PATH + '/ticker',
            params=TickerParams(
                symbol=symbol,
            ),
        )

    async def fetch_tickers(self: 'BaseClient') -> list[dict]:
        """
        Fetch all transaction pair ticker information
        """
        return await self.get(url=SPOT_MARKET_PATH + '/tickers')

    async def fetch_public_trades(
            self: 'BaseClient',
            symbol: str,
            limit: str | None = None,
    ) -> list[dict]:
        """
        Fetch public trading records
        """
        return await self.get(
            url=SPOT_MARKET_PATH + '/fills',
            params=PublicTradeParams(
                symbol=symbol,
                limit=limit,
            ),
        )

    async def fetch_candles(
            self: 'BaseClient',
            symbol: str,
            period: Interval | str,
            after: str | None = None,  # Time after, milliseconds
            before: str | None = None,  # Time before, milliseconds
            limit: str | None = None,  # Default 100
    ) -> list[dict]:
        """
        Fetch candlestick line data
        """
        return await self.get(
            url=SPOT_MARKET_PATH + '/candles',
            params=CandlesParams(
                symbol=symbol,
                period=period,
                after=after,
                before=before,
                limit=limit,
            ),
        )

    async def fetch_order_book(
            self: 'BaseClient',
            symbol: str,
            book_type: OrderBookType,
            limit: str | None = None,
    ) -> dict:
        """
        Fetch order book
        """
        return await self.get(
            url=SPOT_MARKET_PATH + '/depth',
            params=OrderBookParams(
                symbol=symbol,
                book_type=book_type,
                limit=limit,
            ),
        )
