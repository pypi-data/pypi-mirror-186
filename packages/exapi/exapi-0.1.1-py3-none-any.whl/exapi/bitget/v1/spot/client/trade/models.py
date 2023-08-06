from exapi.bitget.v1.enums import OrderType, TimeInForce, TriggerType
from exapi.bitget.v1.models import BaseModel
from exapi.bitget.v1.spot.enums import Side


class BatchOrderCreateParams(BaseModel):
    side: Side  # Order side buy/sell
    order_type: OrderType  # Order type limit/market
    force: TimeInForce
    price: str | None = None  # Limit price, null if orderType is market
    quantity: str  # Order quantity, base coin when order_type is limit; quote coin when order_type is market
    client_order_id: str | None = None  # Custom order ID, length: 40


class OrderCreateParams(BatchOrderCreateParams):
    symbol: str  # Symbol Id


class BatchOrdersCreateParams(BaseModel):
    symbol: str  # Symbol Id
    order_list: list[BatchOrderCreateParams]  # order data list (max length 50)


class OrderCancelParams(BaseModel):
    symbol: str  # Symbol Id
    order_id: str  # Order ID


class BatchOrdersCancelParams(BaseModel):
    symbol: str  # Symbol Id
    order_ids: list[str]  # Order ID array


class OrderParams(BaseModel):
    symbol: str  # Symbol Id


class OrderDetailsParams(OrderParams):
    order_id: str  # Order ID
    client_order_id: str | None = None  # Custom ID


class OrdersHistoryParams(BaseModel):
    symbol: str  # Symbol Id
    after: str | None = None  # orderId, return the data less than or equals this orderId
    before: str | None = None  # orderId, return the data greater than or equals to this orderId
    limit: int | None = None  # The number of returned results, the default is 100, the max. is 500


class OrderFillsParams(BaseModel):
    symbol: str  # Symbol Id
    order_id: str | None = None  # Order ID
    after: str | None = None  # Send in orderId, the data before this orderId desc
    before: str | None = None  # Send in the orderId, the data after this orderId asc
    limit: int | None = None  # The number of returned results, the default is 100, the max. is 500


class OrderPlanCreateParams(BaseModel):
    symbol: str  # Symbol Id
    side: Side  # order side, buy/sell
    trigger_price: float  # order trigger price
    execute_price: float | None = None  # order execute price
    size: float  # purchase quantity, base coin amount when orderType=limit, quote coin amount when orderType=market
    trigger_type: TriggerType  # order trigger type (fill_price/market_price )
    order_type: OrderType  # order type (limit/market)
    client_oid: str | None = None  # Customized client order ID, idempotent control
    time_in_force_value: str | None = None  # Order validity


class OrderPlanUpdateParams(BaseModel):
    order_id: str  # order ID
    trigger_price: float  # order trigger price
    execute_price: float | None = None  # order execute price
    size: str | None = None  # purchase quantity
    order_type: OrderType  # order type (limit/market )


class OrderPlanCancelParams(BaseModel):
    order_id: str  # order ID


class OrderPlanParams(BaseModel):
    symbol: str  # Symbol Id
    page_size: str | None = None  # Page Size
    last_end_id: str | None = None  # last end ID （Pagination needs）


class HistoryOrderPlanParams(BaseModel):
    symbol: str  # Symbol Id
    page_size: str  # Page Size
    last_end_id: str | None = None  # last end ID （Pagination needs)
    start_time: str  # start time
    end_time: str  # end time
