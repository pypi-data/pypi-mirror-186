from uuid import UUID

from exapi.bybit.v3.enums import AccountType, Coin
from exapi.bybit.v3.asset.enums import TransferType
from exapi.bybit.v3.models import BaseModel


class InternalTransferCreateParams(BaseModel):
    transfer_id: UUID | str  # UUID, which is unique across the platform
    coin: Coin | str  # Currency type
    amount: str  # Exchange to amount
    from_account_type: AccountType | str  # Account type
    to_account_type: AccountType | str  # Account type


class SubAccountTransferCreateParams(BaseModel):
    transfer_id: UUID  # UUID, which is unique across the platform
    coin: Coin | str  # Currency type
    amount: str  # Exchange to amount
    sub_member_id: str  # Subaccount
    type: TransferType  # Determines the direction of transfer
