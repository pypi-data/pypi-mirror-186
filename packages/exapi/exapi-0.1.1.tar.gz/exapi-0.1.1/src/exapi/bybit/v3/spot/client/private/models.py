from pydantic import root_validator

from exapi.bybit.v3.enums import Side, Symbol
from exapi.bybit.v3.models import BaseModel
from exapi.bybit.v3.spot.enums import OrderType, TimeInForce


class OrderCreateParams(BaseModel):
    symbol: Symbol | str  # Name of the trading pair
    order_qty: str  # market orders: if side is Buy, this is in the quote currency. Otherwise, in the base currency
    side: Side  # Side. Buy, Sell
    order_type: OrderType  # Order type
    time_in_force: TimeInForce | None = None  # Time in force
    order_price: str | None = None  # When the type field is LIMIT or LIMIT_MAKER, the price field is required
    order_link_id: str | None = None  # User-generated order ID
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order
    trigger_price: str | None = None  # Trigger price


class OrderParams(BaseModel):
    order_id: str | None = None  # Order ID. Required if not passing orderLinkId
    order_link_id: str | None = None  # Unique user-set order ID. Required if not passing orderId
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order.

    @root_validator(pre=True)
    def check_required(cls, values):
        order_id, order_link_id = values.get('order_id'), values.get('order_link_id')
        if order_id is None and order_link_id is None:
            raise ValueError('Required order_id or order_link_id')
        return values


class OrdersCancelParams(BaseModel):
    symbol: Symbol | str  # Name of the trading pair
    side: Side | None = None  # Side. Buy, Sell
    order_types: OrderType | str = None  # LIMIT in default. Allows multiple, separated by comma, e.a LIMIT,LIMIT_MAKER
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order.


class OrdersCancelByIdParams(BaseModel):
    order_ids: str  # Order ID, use commas to indicate multiple orderIds. Maximum of 100 ids.
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order.


class OpenOrdersParams(BaseModel):
    symbol: Symbol | str | None = None  # Name of the trading pair
    order_id: str | None = None  # return all the orders that orderId of which are smaller than this
    limit: int | str | None = None  # Default value is 500, max 500
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order.


class OrdersHistoryParams(BaseModel):
    symbol: Symbol | str | None = None  # Name of the trading pair
    order_id: str | None = None  # return all the orders that orderId of which are smaller than this
    limit: int | str | None = None  # Default value is 100, max 500
    start_time: int | None = None  # Start time, unit in millisecond
    end_time: int | None = None  # End time, unit in millisecond
    order_category: int = 0  # 0：normal order by default; 1：TP/SL order, Required for TP/SL order.


class TradesHistoryParams(BaseModel):
    symbol: Symbol | str | None = None  # Name of the trading pair
    order_id: str | None = None  # return all the orders that orderId of which are smaller than this
    limit: int | str | None = None  # Default value is 50, max 50
    start_time: int | None = None  # Start time, unit in millisecond
    end_time: int | None = None  # End time, unit in millisecond
    from_trade_id: str | None = None  # Query greater than the trade ID. (fromTicketId < trade ID)
    to_trade_id: str | None = None  # Query smaller than the trade ID. (trade ID < toTicketId)
