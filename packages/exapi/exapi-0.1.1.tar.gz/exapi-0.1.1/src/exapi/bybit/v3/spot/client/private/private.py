from exapi.bybit.v3.enums import Side, Symbol
from exapi.bybit.v3.client import BaseClient
from exapi.bybit.v3.constants import SPOT_PRIVATE_PATH
from exapi.bybit.v3.spot.client.private.models import (
    OpenOrdersParams,
    OrderCreateParams,
    OrderParams,
    OrdersCancelByIdParams,
    OrdersCancelParams,
    OrdersHistoryParams,
    TradesHistoryParams,
)
from exapi.bybit.v3.spot.enums import OrderType, TimeInForce


class Private:

    async def create_order(
            self: 'BaseClient',
            symbol: Symbol | str,
            side: Side,
            order_qty: str,
            order_type: OrderType,
            time_in_force: TimeInForce | None = None,
            order_price: str | None = None,
            order_link_id: str | None = None,
            order_category: int = 0,
            trigger_price: str | None = None,
    ) -> dict:
        """
        Create Order
        """
        return await self.post(
            url=SPOT_PRIVATE_PATH + '/order',
            json=OrderCreateParams(
                symbol=symbol,
                side=side,
                order_qty=order_qty,
                order_type=order_type,
                time_in_force=time_in_force,
                order_price=order_price,
                order_link_id=order_link_id,
                order_category=order_category,
                trigger_price=trigger_price,
            ),
            auth=True,
        )

    async def fetch_order(
            self: 'BaseClient',
            order_id: str | None = None,
            order_link_id: str | None = None,
            order_category: int = 0,
    ) -> dict:
        """
        Fetch Order
        """
        return await self.get(
            url=SPOT_PRIVATE_PATH + '/order',
            params=OrderParams(
                order_id=order_id,
                order_link_id=order_link_id,
                order_category=order_category,
            ),
            auth=True,
        )

    async def cancel_order(
            self: 'BaseClient',
            order_id: str | None = None,
            order_link_id: str | None = None,
            order_category: int = 0,
    ) -> dict:
        """
        Cancel Order
        """
        return await self.post(
            url=SPOT_PRIVATE_PATH + '/cancel-order',
            json=OrderParams(
                order_id=order_id,
                order_link_id=order_link_id,
                order_category=order_category,
            ),
            auth=True,
        )

    async def cancel_orders(
            self: 'BaseClient',
            symbol: Symbol | str,
            side: Side | None = None,
            order_types: OrderType | str = None,
            order_category: int = 0,
    ) -> dict:
        """
        Batch Cancel Orders
        """
        return await self.post(
            url=SPOT_PRIVATE_PATH + '/cancel-orders',
            json=OrdersCancelParams(
                symbol=symbol,
                side=side,
                order_types=order_types,
                order_category=order_category,
            ),
            auth=True,
        )

    async def cancel_orders_by_ids(
            self: 'BaseClient',
            order_ids: str,
            order_category: int = 0,
    ) -> list[dict]:
        """
        Batch Cancel Orders By IDs
        """
        return await self.post(
            url=SPOT_PRIVATE_PATH + '/cancel-orders-by-ids',
            json=OrdersCancelByIdParams(
                order_ids=order_ids,
                order_category=order_category,
            ),
            auth=True,
        )

    async def fetch_open_orders(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
            order_id: str | None = None,
            limit: int | str | None = None,
            order_category: int = 0,
    ) -> list[dict]:
        """
        Fetch Open Orders
        """
        return await self.get(
            url=SPOT_PRIVATE_PATH + '/open-orders',
            params=OpenOrdersParams(
                symbol=symbol,
                order_id=order_id,
                limit=limit,
                order_category=order_category,
            ),
            auth=True,
        )

    async def fetch_orders_history(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
            order_id: str | None = None,
            limit: int | str | None = None,
            start_time: int | None = None,
            end_time: int | None = None,
            order_category: int = 0,
    ) -> list[dict]:
        """
        Fetch Orders History
        """
        return await self.get(
            url=SPOT_PRIVATE_PATH + '/history-orders',
            params=OrdersHistoryParams(
                symbol=symbol,
                order_id=order_id,
                limit=limit,
                start_time=start_time,
                end_time=end_time,
                order_category=order_category,
            ),
            auth=True,
        )

    async def fetch_trades_history(
            self: 'BaseClient',
            symbol: Symbol | str | None = None,
            order_id: str | None = None,
            start_time: int | None = None,
            end_time: int | None = None,
            from_trade_id: str | None = None,
            to_trade_id: str | None = None,
            limit: int | str | None = None,
    ) -> list[dict]:
        """
        Fetch Trades History
        """
        return await self.get(
            url=SPOT_PRIVATE_PATH + '/my-trades',
            params=TradesHistoryParams(
                symbol=symbol,
                order_id=order_id,
                start_time=start_time,
                end_time=end_time,
                from_trade_id=from_trade_id,
                to_trade_id=to_trade_id,
                limit=limit,
            ),
            auth=True,
        )

    async def fetch_account_wallet(self: 'BaseClient') -> dict:
        """
        Fetch Account Balances
        """
        return await self.get(
            url=SPOT_PRIVATE_PATH + '/account',
            auth=True,
        )
