from time import time
from uuid import UUID

from exapi.bybit.v3.enums import AccountType, Coin
from exapi.bybit.v3.asset.enums import TransferType
from exapi.bybit.v3.asset.models import InternalTransferCreateParams, SubAccountTransferCreateParams
from exapi.bybit.v3.client import BaseClient
from exapi.bybit.v3.constants import ASSET_PRIVATE_PATH, PUBLIC_PATH


class AssetClient(BaseClient):

    async def sync_time(self) -> None:
        public_time = await self.fetch_public_time()
        timestamp = int(time())
        if public_time['timeSecond'] - self._recv_window <= timestamp < public_time['timeSecond'] + 1000:
            return
        raise RuntimeError('Need update local time')

    async def fetch_public_time(self) -> dict:
        """
        Fetch public time
        """
        return await self.get(url=PUBLIC_PATH + '/time')

    async def create_internal_transfer(
            self,
            transfer_id: UUID | str,
            coin: Coin | str,
            amount: str,
            from_account_type: AccountType | str,
            to_account_type: AccountType | str,
    ) -> dict:
        """
        Create Internal Transfer
        """
        return await self.post(
            url=ASSET_PRIVATE_PATH + '/transfer/inter-transfer',
            params=InternalTransferCreateParams(
                transfer_id=transfer_id,
                coin=coin,
                amount=amount,
                from_account_type=from_account_type,
                to_account_type=to_account_type,
            ),
            auth=True,
        )

    async def create_sub_account_transfer(
            self,
            transfer_id: UUID,
            coin: Coin | str,
            amount: str,
            sub_member_id: str,
            transfer_type: TransferType,
    ) -> dict:
        """
        Create SubAccount Transfer
        """
        return await self.post(
            url=ASSET_PRIVATE_PATH + '/transfer/sub-member-transfer',
            params=SubAccountTransferCreateParams(
                transfer_id=transfer_id,
                coin=coin,
                amount=amount,
                sub_member_id=sub_member_id,
                type=transfer_type,
            ),
            auth=True,
        )
