from exapi.bitget.v1.models import BaseModel
from exapi.bitget.v1.spot.enums import AccountType, BusinessType, GroupType


class AssetsParams(BaseModel):
    coin: str = None


class BillParams(BaseModel):
    coin_id: int | None = None  # Coin ID
    group_type: GroupType | None = None  # Transaction group type groupType
    biz_type: BusinessType | None = None  # Business type bizType
    after: str | None = None  # BillId, return the data less than this billId
    before: str | None = None  # BillId, return the data greater than this billId
    limit: int | None = None  # The number of returned results, the default is 100, the max. is 500


class TransfersParams(BaseModel):
    coin_id: int | None = None  # Coin ID
    from_type: AccountType | None = None  # Major type of bill accountType
    after: str | None = None  # BillId, the data less or equals or equals to 'tradeTime', seconds
    before: str | None = None  # BillId, the data greater than or equals 'tradeTime', seconds
    limit: int | None = None  # The number of returned results, the default is 100, the max. is 500
