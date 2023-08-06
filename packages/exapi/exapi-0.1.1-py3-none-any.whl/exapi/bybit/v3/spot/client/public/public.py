from exapi.bybit.v3.enums import Interval, Symbol
from exapi.bybit.v3.client import BaseClient
from exapi.bybit.v3.constants import SPOT_PUBLIC_PATH
from exapi.bybit.v3.spot.client.public.models import (
    BookTickerParams,
    CandlesParams,
    MergedOrderBookParams,
    OrderBookParams,
    PublicTradeParams,
    SymbolInfoParams,
    TickerPriceParams,
)


class Public:

    async def fetch_server_time(self: 'BaseClient') -> dict:
        """
        Fetch server time
        """
        return await self.get(url=SPOT_PUBLIC_PATH + '/server-time')

    async def fetch_symbols(self: 'BaseClient') -> list[dict]:
        """
        Fetch All Symbols
        """
        return await self.get(url=SPOT_PUBLIC_PATH + '/symbols')

    async def fetch_order_book(
            self: 'BaseClient',
            symbol: Symbol | str,
            limit: int | None = None,
    ) -> dict:
        """
        Fetch Order Book
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/depth',
            params=OrderBookParams(
                symbol=symbol,
                limit=limit,
            ),
        )

    async def fetch_merged_order_book(
            self: 'BaseClient',
            symbol: Symbol | str,
            scale: int | None = None,
            limit: int | None = None,
    ) -> dict:
        """
        Fetch merged orderbook

        :param symbol: Name of the trading pair
        :param scale: Precision of the merged orderbook, 1 means 1 digit
        :param limit: Default value is 100
        :return: dict
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/depth/merged',
            params=MergedOrderBookParams(
                symbol=symbol,
                scale=scale,
                limit=limit,
            ),
        )

    async def fetch_public_trades(
            self: 'BaseClient',
            symbol: Symbol | str,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch public trading records

        :param symbol: Name of the trading pair
        :param limit: Default value is 60, max 60
        :return: List of dict
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/trades',
            params=PublicTradeParams(
                symbol=symbol,
                limit=limit,
            ),
        )

    async def fetch_candles(
            self: 'BaseClient',
            symbol: Symbol | str,
            interval: Interval | str,
            start_time: int | None = None,
            end_time: int | None = None,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch candles
        info: It only returns the results from latest 3500 candles regardless of what interval is specified
        info: If startTime and endTime are not specified, only the latest candles will be sent

        :return: List of dict
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/kline',
            params=CandlesParams(
                symbol=symbol,
                interval=interval,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
            ),
        )

    async def fetch_symbol_info(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
    ) -> dict | list[dict]:
        """
        Fetch the latest information for symbol
        info: If symbol is not specified, the data from all symbols will be returned

        :param symbol: Name of the trading pair
        :return: dict or List of dict if symbol not specified
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/ticker/24hr',
            params=SymbolInfoParams(
                symbol=symbol,
            ),
        )

    async def fetch_ticker_price(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
    ) -> dict | list[dict]:
        """
        Fetch the latest traded price
        info: If symbol is not specified, the data from all symbols will be returned

        :param symbol: Name of the trading pair
        :return: dict or List of dict if symbol not specified
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/ticker/price',
            params=TickerPriceParams(
                symbol=symbol,
            ),
        )

    async def fetch_book_ticker(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
    ) -> dict | list[dict]:
        """
        Fetch the best Bid/Ask price
        info: If symbol is not specified, the data from all symbols will be returned

        :param symbol: Name of the trading pair
        :return: dict or List of dict if symbol not specified
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/quote/ticker/bookTicker',
            params=BookTickerParams(
                symbol=symbol,
            ),
        )
