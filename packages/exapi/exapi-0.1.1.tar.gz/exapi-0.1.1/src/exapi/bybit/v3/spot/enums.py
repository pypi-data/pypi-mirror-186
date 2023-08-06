from enum import Enum


class TimeInForce(str, Enum):
    GTC = 'GTC'  # Good Till Canceled
    FOK = 'FOK'  # Fill or Kill
    IOC = 'IOC'  # Immediate or Cancel


class OrderType(str, Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    LIMIT_MAKER = 'LIMIT_MAKER'


class OrderStatus(str, Enum):
    NEW = 'NEW'
    PARTIALLY_FILLED = 'PARTIALLY_FILLED'
    FILLED = 'FILLED'
    CANCELED = 'CANCELED'
    PENDING_CANCEL = 'PENDING_CANCEL'
    PENDING_NEW = 'PENDING_NEW'
    REJECTED = 'REJECTED'
