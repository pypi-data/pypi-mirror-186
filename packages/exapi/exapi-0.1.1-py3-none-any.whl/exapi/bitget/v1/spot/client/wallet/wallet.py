from exapi.bitget.v1 import BaseClient
from exapi.bitget.v1.constants import SPOT_WALLET_PATH
from exapi.bitget.v1.enums import TransferType
from exapi.bitget.v1.spot.client.wallet.models import (
    DepositParams,
    InnerWithdrawalParams,
    SubTransferCreateParams,
    TransferCreateParams,
    WalletParams,
    WithdrawalCreateParams,
    WithdrawalsParams,
)


class Wallet:

    async def create_transfer(
            self: 'BaseClient',
            from_type: TransferType,
            to_type: TransferType,
            amount: str,
            coin: str,
            client_oid: str | None = None,
    ) -> None:
        """
        Create inner transfer
        """
        await self.post(
            url=SPOT_WALLET_PATH + '/transfer',
            json=TransferCreateParams(
                from_type=from_type,
                to_type=to_type,
                amount=amount,
                coin=coin,
                client_oid=client_oid,
            ),
            auth=True,
        )

    async def create_sub_transfer(
            self: 'BaseClient',
            from_type: TransferType,
            to_type: TransferType,
            amount: str,
            coin: str,
            client_oid: str,
            from_user_id: str,
            to_user_id: str,
    ) -> None:
        """
        Create sub account transfer
        """
        await self.post(
            url=SPOT_WALLET_PATH + '/subTransfer',
            json=SubTransferCreateParams(
                from_type=from_type,
                to_type=to_type,
                amount=amount,
                coin=coin,
                client_oid=client_oid,
                from_user_id=from_user_id,
                to_user_id=to_user_id,
            ),
            auth=True,
        )

    async def fetch_deposit_wallet(
            self: 'BaseClient',
            coin: str,
            chain: str,
    ) -> dict:
        """
        Fetch Coin Address
        """
        return await self.get(
            url=SPOT_WALLET_PATH + '/deposit-address',
            params=WalletParams(
                coin=coin,
                chain=chain,
            ),
            auth=True,
        )

    async def create_withdrawal(
            self: 'BaseClient',
            coin: str,
            address: str,
            chain: str,
            amount: str,
            tag: str | None = None,
            remark: str | None = None,
            client_oid: str | None = None,
    ) -> str:
        """
        Create withdraw coins on the chain
        """
        return await self.post(
            url=SPOT_WALLET_PATH + '/withdrawal',
            json=WithdrawalCreateParams(
                coin=coin,
                address=address,
                chain=chain,
                amount=amount,
                tag=tag,
                remark=remark,
                client_oid=client_oid,
            ),
            auth=True,
        )

    async def create_inner_withdrawal(
            self: 'BaseClient',
            coin: str,
            to_uid: str,
            amount: str,
            client_oid: str | None = None,
    ) -> str:
        """
        Create internal withdrawal means that both users are on the Bitget platform
        """
        return await self.post(
            url=SPOT_WALLET_PATH + '/withdrawal-inner',
            json=InnerWithdrawalParams(
                coin=coin,
                to_uid=to_uid,
                amount=amount,
                client_oid=client_oid,
            ),
            auth=True,
        )

    async def fetch_withdrawals(
            self: 'BaseClient',
            coin: str,
            start_time: str,
            end_time: str,
            page_no: str | None = None,
            page_size: str | None = None,
    ) -> list[dict]:
        """
        Fetch withdrawal list
        """
        return await self.get(
            url=SPOT_WALLET_PATH + '/withdrawal-list',
            params=WithdrawalsParams(
                coin=coin,
                start_time=start_time,
                end_time=end_time,
                page_no=page_no,
                page_size=page_size,
            ),
            auth=True,
        )

    async def fetch_deposits(
            self: 'BaseClient',
            coin: str,
            start_time: str,
            end_time: str,
            page_no: str | None = None,
            page_size: str | None = None,
    ) -> list[dict]:
        """
        Fetch deposit list
        """
        return await self.get(
            url=SPOT_WALLET_PATH + '/deposit-list',
            params=DepositParams(
                coin=coin,
                start_time=start_time,
                end_time=end_time,
                page_no=page_no,
                page_size=page_size,
            ),
            auth=True,
        )
