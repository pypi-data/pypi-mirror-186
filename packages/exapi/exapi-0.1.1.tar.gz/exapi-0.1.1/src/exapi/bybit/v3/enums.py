from enum import Enum


class Side(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class Symbol(str, Enum):
    ADAUSDT = 'ADAUSDT'
    ATOMUSDT = 'ATOMUSDT'
    BTCUSDT = 'BTCUSDT'
    ETHUSDT = 'ETHUSDT'
    BITUSDT = 'BITUSDT'
    BNBUSDT = 'BNBUSDT'
    ETCUSDT = 'ETCUSDT'
    LTCUSDT = 'LTCUSDT'
    DOGEUSDT = 'DOGEUSDT'
    KASTAUSDT = 'KASTAUSDT'
    MATICUSDT = 'MATICUSDT'
    SOLUSDT = 'SOLUSDT'
    SHIBUSDT = 'SHIBUSDT'
    TRXUSDT = 'TRXUSDT'
    XRPUSDT = 'XRPUSDT'
    XTZUSDT = 'XTZUSDT'


class Coin(str, Enum):
    BTC = 'BTC'
    ETH = 'ETH'
    USDT = 'USDT'


class Interval(str, Enum):
    TF_1m = '1m'
    TF_3m = '3m'
    TF_5m = '5m'
    TF_15m = '15m'
    TF_30m = '30m'
    TF_1H = '1h'
    TF_2H = '2h'
    TF_4H = '4h'
    TF_6H = '6h'
    TF_12H = '12h'
    TF_1D = '1d'
    TF_1W = '1w'
    TF_1M = '1M'


class AccountType(str, Enum):
    CONTRACT = 'CONTRACT'
    SPOT = 'SPOT'
    INVESTMENT = 'INVESTMENT'  # ByFi Account
    OPTION = 'OPTION'  # USDC Account
    UNIFIED = 'UNIFIED'


class Operation(str, Enum):
    AUTH = 'auth'
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'
