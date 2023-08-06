from exapi.bitget.v1 import BaseClient
from exapi.bitget.v1.constants import SPOT_ACCOUNT_PATH
from exapi.bitget.v1.spot.client.account.models import (
    TransfersParams,
    AssetsParams,
    BillParams,
)
from exapi.bitget.v1.spot.enums import AccountType, BusinessType, GroupType


class Account:

    async def fetch_api_key_info(self: 'BaseClient') -> dict:
        """
        Fetch ApiKey Info
        """
        return await self.get(
            url=SPOT_ACCOUNT_PATH + '/getInfo',
            auth=True,
        )

    async def fetch_assets(
            self: 'BaseClient',
            coin: str = None,
    ) -> dict | list[dict]:
        """
        Fetch Account Assets
        """
        return await self.get(
            url=SPOT_ACCOUNT_PATH + '/assets',
            params=AssetsParams(
                coin=coin,
            ),
            auth=True,
        )

    async def fetch_spot_assets(self: 'BaseClient') -> list[dict]:
        """
        Fetch sub Account Spot Assets
        """
        return await self.post(
            url=SPOT_ACCOUNT_PATH + '/sub-account-spot-assets',
            auth=True,
        )

    async def fetch_bills(
            self: 'BaseClient',
            coin_id: int | None = None,
            group_type: GroupType | None = None,
            business_type: BusinessType | None = None,
            after: str | None = None,
            before: str | None = None,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch all asset currency information of the user
        """
        return await self.post(
            url=SPOT_ACCOUNT_PATH + '/bills',
            json=BillParams(
                coin_id=coin_id,
                group_type=group_type,
                biz_type=business_type,
                after=after,
                before=before,
                limit=limit,
            ),
            auth=True,
        )

    async def fetch_transfers(
            self: 'BaseClient',
            coin_id: int | None = None,
            from_type: AccountType | None = None,
            after: str | None = None,
            before: str | None = None,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch account transfers
        """
        return await self.get(
            url=SPOT_ACCOUNT_PATH + '/transferRecords',
            params=TransfersParams(
                coin_id=coin_id,
                from_type=from_type,
                after=after,
                before=before,
                limit=limit,
            ),
            auth=True,
        )
