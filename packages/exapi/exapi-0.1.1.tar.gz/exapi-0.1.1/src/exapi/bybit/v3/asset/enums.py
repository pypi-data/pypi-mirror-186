from enum import Enum


class WithdrawStatus(str, Enum):
    SECURITY_CHECK = 'SecurityCheck'
    PENDING = 'Pending'
    SUCCESS = 'success'
    CANCEL_BY_USER = 'CancelByUser'
    REJECT = 'Reject'
    FAIL = 'Fail'
    BLOCKCHAIN_CONFIRMED = 'BlockchainConfirmed'


class OperatorType(str, Enum):
    SYSTEM = 'SYSTEM'
    USER = 'USER'
    ADMIN = 'ADMIN'
    AFFILIATE_USER = 'AFFILIATE_USER'


class TransferType(str, Enum):
    IN = 'IN'  # transfer from main account to subaccount
    OUT = 'OUT'  # transfer from subaccount to main account


class TransferStatus(str, Enum):
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'
    FAILED = 'FAILED'


class PageDirection(str, Enum):
    PREV = 'Prev'
    NEXT = 'Next'
