from exapi.bitget.v1.enums import TransferType
from exapi.bitget.v1.models import BaseModel


class TransferCreateParams(BaseModel):
    from_type: TransferType  # out account type
    to_type: TransferType  # inner account type
    amount: str  # transfer amount
    coin: str  # transfer coin
    client_oid: str | None = None  # custom id


class SubTransferCreateParams(BaseModel):
    from_type: TransferType  # from account type
    to_type: TransferType  # to account type
    amount: str  # transfer amount
    coin: str  # transfer coin
    client_oid: str  # unique custom id, idempotent control
    from_user_id: str  # from user ID
    to_user_id: str  # to user ID


class WalletParams(BaseModel):
    coin: str  # currency name
    chain: str  # chain name


class WithdrawalCreateParams(BaseModel):
    coin: str  # currency name
    address: str  # withdraw address
    chain: str  # chain name
    tag: str | None = None  # tag
    amount: str  # Withdraw amount
    remark: str | None = None
    client_oid: str | None = None  # custom id


class InnerWithdrawalParams(BaseModel):
    coin: str  # currency
    to_uid: str  # target uid
    amount: str  # Withdraw amount
    client_oid: str | None = None  # custom id


class WithdrawalsParams(BaseModel):
    coin: str  # currency
    start_time: str  # start Time (timestamp ms)
    end_time: str  # end Time(timestamp ms)
    page_no: str | None = None  # pageNo default 1
    page_size: str | None = None  # pageSize default 20, max 100


class DepositParams(WithdrawalsParams):
    pass
