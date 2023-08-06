from enum import Enum


class Side(str, Enum):
    BUY = 'buy'
    SELL = 'sell'


class Interval(str, Enum):
    TF_1m = '1min'
    TF_5m = '5min'
    TF_15m = '15min'
    TF_30m = '30min'
    TF_1H = '1h'
    TF_4H = '4h'
    TF_6H = '6h'
    TF_12H = '12h'
    TF_1D = '1day'
    TF_3D = '3day'
    TF_1W = '1week'
    TF_1M = '1M'
    UTC_6H = '6Hutc'  # UTC0 6 hour
    UTC_12H = '12Hutc'  # UTC0 12 hour
    UTC_1D = '1Dutc'  # UTC0 1 day
    UTC_3D = '3Dutc'  # UTC0 3 day
    UTC_1W = '1Wutc'  # UTC0 1 week
    UTC_1M = '1Mutc'  # UTC0 1 month


class OrderStatus(str, Enum):
    INIT = 'init'  # Initial, inserted into DB
    NEW = 'new'  # Unfilled, pending in orderbook
    PARTIAL_FILL = 'partial_fill'  # Partially filled
    FULL_FILL = 'full_fill'  # Fully filled
    CANCELLED = 'cancelled'  # Cancelled


# Major types of transaction
class GroupType(str, Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSACTION = 'transaction'
    TRANSFER = 'transfer'
    OTHER = 'other'


class BusinessType(str, Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    BUY = 'buy'
    SELL = 'sell'
    DEDUCTION_OF_HANDLING_FEE = 'deduction of handling fee'
    TRANSFER_IN = 'transfer-in'
    TRANSFER_OUT = 'transfer-out'
    REBATE_REWARDS = 'rebate rewards'
    AIRDROP_REWARDS = 'airdrop rewards'
    USDT_CONTRACT_REWARDS = 'USDT contract rewards'
    MIX_CONTRACT_REWARDS = 'mix contract rewards'
    SYSTEM_LOCK = 'System lock'
    USER_LOCK = 'User lock'


class DepositStatus(str, Enum):
    CANCEL = 'cancel'
    REJECT = 'reject'
    SUCCESS = 'success'
    WALLET_FAIL = 'wallet-fail'
    WALLET_PROCESSING = 'wallet-processing'
    FIRST_AUDIT = 'first-audit'
    RECHECK = 'recheck'
    FIRST_REJECT = 'first-reject'
    RECHECK_REJECT = 'recheck-reject'


class WithdrawalStatus(str, Enum):
    PENDING = 'pending'
    PENDING_REVIEW = 'pending_review'
    PENDING_FAIL = 'pending_fail'
    PENDING_REVIEW_FAIL = 'pending_review_fail'
    REJECT = 'reject'
    SUCCESS = 'success'


class WithdrawalType(str, Enum):
    CHAIN_ON = 'chain-on'
    INNER_TRANSFER = 'inner-transfer'


class AccountType(str, Enum):
    EXCHANGE = 'EXCHANGE'
    OTC_SGD = 'OTC_SGD'
    CONTRACT = 'CONTRACT'
    USD_MIX = 'USD_MIX'
    USDT_MIX = 'USDT_MIX'


class OrderBookType(str, Enum):
    STEP_0 = 'step0'
    STEP_1 = 'step1'
    STEP_2 = 'step2'
    STEP_3 = 'step3'
    STEP_4 = 'step4'
    STEP_5 = 'step5'
