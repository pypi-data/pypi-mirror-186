from enum import Enum


class AccountStatus(str, Enum):
    NORMAL = 'normal'
    FREEZE = 'freeze'
    DEL = 'del'


class Authority(str, Enum):
    WITHDRAW = 'withdraw'
    RECHARGE = 'recharge'
    TRANSFER = 'transfer'
    SPOT_TRADE = 'spot_trade'
    CONTRACT_TRADE = 'contract_trade'
    READONLY = 'readonly'
