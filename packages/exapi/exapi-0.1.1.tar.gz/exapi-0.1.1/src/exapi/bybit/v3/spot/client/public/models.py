from exapi.bybit.v3.enums import Interval, Symbol
from exapi.bybit.v3.models import BaseModel


class OrderBookParams(BaseModel):
    symbol: Symbol | str
    limit: int | None = None


class MergedOrderBookParams(OrderBookParams):
    scale: int | None = None


class PublicTradeParams(BaseModel):
    symbol: Symbol | str
    limit: int | None = None


class CandlesParams(BaseModel):
    symbol: Symbol | str  # Name of the trading pair
    interval: Interval | str  # Chart interval
    start_time: int | None = None  # Start time, unit in millisecond
    end_time: int | None = None  # End time, unit in millisecond
    limit: int | None = None  # Default value is 1000, max 1000


class SymbolInfoParams(BaseModel):
    symbol: Symbol | str | None = None


class TickerPriceParams(BaseModel):
    symbol: Symbol | str | None = None


class BookTickerParams(BaseModel):
    symbol: Symbol | str | None = None
