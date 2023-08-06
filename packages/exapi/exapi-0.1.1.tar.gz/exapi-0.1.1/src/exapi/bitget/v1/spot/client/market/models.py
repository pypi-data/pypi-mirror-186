from exapi.bitget.v1.models import BaseModel
from exapi.bitget.v1.spot.enums import Interval, OrderBookType


class TickerParams(BaseModel):
    symbol: str


class PublicTradeParams(BaseModel):
    symbol: str
    limit: str | None = None


class CandlesParams(BaseModel):
    symbol: str
    period: Interval | str
    after: str | None = None  # Time after, milliseconds
    before: str | None = None  # Time before, milliseconds
    limit: str | None = None  # Default 100


class OrderBookParams(BaseModel):
    symbol: str
    book_type: OrderBookType
    limit: str | None = None
