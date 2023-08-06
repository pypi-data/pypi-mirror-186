from enum import Enum


class Interval(str, Enum):
    TF_1m = '1m'
    TF_3m = '3m'
    TF_5m = '5m'
    TF_15m = '15m'
    TF_30m = '30m'
    TF_1H = '1H'
    TF_2H = '2H'
    TF_4H = '4H'
    TF_6H = '6H'
    TF_12H = '12H'
    TF_1D = '1D'
    TF_3D = '3D'
    TF_1W = '1W'
    TF_1M = '1M'
    UTC_6H = '6Hutc'  # UTC0 6 hour
    UTC_12H = '12Hutc'  # UTC0 12 hour
    UTC_1D = '1Dutc'  # UTC0 1 day
    UTC_3D = '3Dutc'  # UTC0 3 day
    UTC_1W = '1Wutc'  # UTC0 1 week
    UTC_1M = '1Mutc'  # UTC0 1 month


# Position Mode
class HoldMode(str, Enum):
    SINGLE_HOLD = 'single_hold'  # One-way position
    DOUBLE_HOLD = 'double_hold'  # Two-way position


# Position Direction
class HoldSide(str, Enum):
    LONG = 'long'
    SHORT = 'short'


class BusinessType(str, Enum):
    OPEN_LONG = 'open_long'
    OPEN_SHORT = 'open_short'
    CLOSE_LONG = 'close_long'
    CLOSE_SHORT = 'close_short'
    TRANS_FROM_EXCHANGE = 'trans_from_exchange'  # Transfer in from spot account
    TRANS_TO_EXCHANGE = 'trans_to_exchange'  # Transfer out to spot account
    CONTRACT_MAIN_SETTLE_FEE = 'contract_main_settle_fee'  # Funding rate for crossed
    CONTRACT_MARGIN_SETTLE_FEE = 'contract_margin_settle_fee'  # Fixed margin funding rate
    TRACKING_TRADER_INCOME = 'tracking_trader_income'
    BURST_LONG_LOSS_QUERY = 'burst_long_loss_query'  # Liquidated close long
    BURST_SHORT_LOSS_QUERY = 'burst_short_loss_query'  # Liquidated close short


class Side(str, Enum):
    OPEN_LONG = 'open_long'
    OPEN_SHORT = 'open_short'
    CLOSE_LONG = 'close_long'
    CLOSE_SHORT = 'close_short'
    BUY_SINGLE = 'buy_single'  # Open long under single_hold mode
    SELL_SINGLE = 'sell_single'  # Open short under single_hold mode


class TradeSide(str, Enum):
    # Values for double_hold
    OPEN_LONG = 'open_long'
    OPEN_SHORT = 'open_short'
    CLOSE_LONG = 'close_long'
    CLOSE_SHORT = 'close_short'
    REDUCE_CLOSE_LONG = 'reduce_close_long'  # Force reduce long position
    REDUCE_CLOSE_SHORT = 'reduce_close_short'  # Force reduce short position
    OFFSET_CLOSE_LONG = 'offset_close_long'  # Force netting: close long position
    OFFSET_CLOSE_SHORT = 'offset_close_short'  # Force netting: close short position
    BURST_CLOSE_LONG = 'burst_close_long'  # Force liquidation: close long position
    BURST_CLOSE_SHORT = 'burst_close_short'  # Force liquidation: close short position
    DELIVERY_CLOSE_LONG = 'delivery_close_long'  # Future delivery close long
    DELIVERY_CLOSE_SHORT = 'delivery_close_short'  # Future delivery close short

    # Values for single_hold
    BUY_SINGLE = 'buy_single'  # Buy in single_hold mode
    SELL_SINGLE = 'sell_single'  # Sell in single_hold mode
    REDUCE_BUY_SINGLE = 'reduce_buy_single'  # Force reduce buy in single_hold mode
    REDUCE_SELL_SINGLE = 'reduce_sell_single'  # Force reduce sell in single_hold mode
    BURST_BUY_SINGLE = 'burst_buy_single'  # Force liquidation: buy in single_hold mode
    BURST_SELL_SINGLE = 'burst_sell_single'  # Force liquidation: sell in single_hold mode
    DELIVERY_BUY_SINGLE = 'delivery_buy_single'  # Future delivery buy in single_hold mode
    DELIVERY_SELL_SINGLE = 'delivery_sell_single'  # Future delivery sell in single_hold mode


class OrderStatus(str, Enum):
    INIT = 'init'  # Initial, inserted into DB
    NEW = 'new'  # New order, pending match in orderbook
    PARTIALLY_FILLED = 'partially_filled'  # Partially filled
    FILLED = 'filled'  # Filled
    CANCELED = 'canceled'  # Canceled


class PlanType(str, Enum):
    PROFIT_PLAN = 'profit_plan'
    LOSS_PLAN = 'loss_plan'
    NORMAL_PLAN = 'normal_plan'
    POS_PROFIT = 'pos_profit'
    POS_LOSS = 'pos_loss'
    MOVING_PLAN = 'moving_plan'
    TRACK_PLAN = 'track_plan'


class IsPlan(str, Enum):
    PLAN = 'plan'
    PROFIT_LOSS = 'profit_loss'


class PlanStatus(str, Enum):
    NOT_TRIGGER = 'not_trigger'
    TRIGGERED = 'triggered'
    FAIL_TRIGGER = 'fail_trigger'
    CANCEL = 'cancel'


class StopType(str, Enum):
    PROFIT = 'profit'
    LOSS = 'loss'


class StreamPlanType(str, Enum):
    PL = 'pl'  # default, push data whenever a plan order is created/cancelled/modified/triggered
    TP = 'tp'  # push data when a take profit order(partial position) is created/cancelled/modified/triggered
    SL = 'sl'  # push data when a stop loss order(partial position) is created/cancelled/modified/triggered
    PTP = 'ptp'  # push data when a position take profit order(whole position) is created/cancelled/modified/triggered
    PSL = 'psl'  # push data when a position stop loss order(whole position) is created/cancelled/modified/triggered


class SymbolStatus(str, Enum):
    NORMAL = 'normal'
    MAINTAIN = 'maintain'
    OFF = 'off'
