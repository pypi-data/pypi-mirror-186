from enum import Enum


class ProductType(str, Enum):
    UMCBL = 'umcbl'  # USDT perpetual contract
    DMCBL = 'dmcbl'  # Universal margin perpetual contract
    CMCBL = 'cmcbl'  # USDC perpetual contract
    SUMCBL = 'sumcbl'  # USDT simulation perpetual contract
    SDMCBL = 'sdmcbl'  # Universal margin simulation perpetual contract
    SCMCBL = 'scmcbl'  # USDC simulation perpetual contract


class TransferType(str, Enum):
    SPOT = 'spot'  # spot asset coin
    MIX_USDT = 'mix_usdt'  # USDT transfer only
    MIX_USD = 'mix_usd'  # BTC, ETH, EOS, XRP, USDC
    MIX_USDC = 'mix_usdc'  # USDC transfer only


class MarginMode(str, Enum):
    FIXED = 'fixed'  # Isolated margin crossed Cross margin
    CROSSED = 'crossed'  # Cross margin


class TimeInForce(str, Enum):
    NORMAL = 'normal'  # Good till cancel
    POST_ONLY = 'post_only'  # Maker only
    FOK = 'fok'  # Fill or kill（FOK）
    IOC = 'ioc'  # Immediate or cancel（IOC）


class OrderType(str, Enum):
    LIMIT = 'limit'
    MARKET = 'market'


class TriggerType(str, Enum):
    FILL_PRICE = 'fill_price'
    MARKET_PRICE = 'market_price'


class ApiKeyPermission(str, Enum):
    TRADE = 'trade'
    TRANSFER = 'transfer'
    WITHDRAW = 'withdraw'
    READ_ONLY = 'read_only'


class Operation(str, Enum):
    LOGIN = 'login'
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'
