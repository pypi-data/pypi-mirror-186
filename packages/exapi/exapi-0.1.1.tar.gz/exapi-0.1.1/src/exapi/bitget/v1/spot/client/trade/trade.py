from exapi.bitget.v1 import BaseClient
from exapi.bitget.v1.constants import SPOT_TRADE_PATH
from exapi.bitget.v1.enums import OrderType, TimeInForce, TriggerType
from exapi.bitget.v1.spot.client.trade.models import (
    BatchOrdersCancelParams,
    BatchOrdersCreateParams,
    HistoryOrderPlanParams,
    OrderCancelParams,
    OrderCreateParams,
    OrderDetailsParams,
    OrderFillsParams,
    OrderParams,
    OrderPlanCancelParams,
    OrderPlanCreateParams,
    OrderPlanParams,
    OrderPlanUpdateParams,
    OrdersHistoryParams,
)
from exapi.bitget.v1.spot.enums import Side


class Trade:

    async def create_order(
            self: 'BaseClient',
            symbol: str,
            side: Side,
            order_type: OrderType,
            force: TimeInForce,
            quantity: str,
            price: str | None = None,
            client_order_id: str | None = None,
    ) -> dict:
        """
        Create order
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/orders',
            json=OrderCreateParams(
                symbol=symbol,
                side=side,
                order_type=order_type,
                force=force,
                quantity=quantity,
                price=price,
                client_order_id=client_order_id,
            ),
            auth=True,
        )

    async def create_batch_orders(
            self: 'BaseClient',
            symbol: str,
            order_list: list[dict],
    ) -> dict:
        """
        Create batch orders
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/batch-orders',
            json=BatchOrdersCreateParams(
                symbol=symbol,
                order_list=order_list,
            ),
            auth=True,
        )

    async def cancel_order(
            self: 'BaseClient',
            symbol: str,
            order_id: str,
    ) -> int:
        """
        Cancel order
        """
        result = await self.post(
            url=SPOT_TRADE_PATH + '/cancel-order',
            json=OrderCancelParams(
                symbol=symbol,
                order_id=order_id,
            ),
            auth=True,
        )

        return int(result)

    async def cancel_batch_orders(
            self: 'BaseClient',
            symbol: str,
            order_ids: list[str],
    ) -> int:
        """
        Cancel batch orders
        """
        result = await self.post(
            url=SPOT_TRADE_PATH + '/cancel-batch-orders',
            json=BatchOrdersCancelParams(
                symbol=symbol,
                order_ids=order_ids,
            ),
            auth=True,
        )

        return int(result)

    async def fetch_order_details(
            self: 'BaseClient',
            order_id: str,
            client_order_id: str | None = None,
    ) -> list[dict]:
        """
        Fetch order details
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/orderInfo',
            json=OrderDetailsParams(
                order_id=order_id,
                client_order_id=client_order_id,
            ),
            auth=True,
        )

    async def fetch_orders(
            self: 'BaseClient',
            symbol: str,
    ) -> list[dict]:
        """
        Fetch orders
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/open-orders',
            json=OrderParams(
                symbol=symbol,
            ),
            auth=True,
        )

    async def fetch_orders_history(
            self: 'BaseClient',
            symbol: str,
            after: str | None = None,
            before: str | None = None,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch orders history
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/history',
            json=OrdersHistoryParams(
                symbol=symbol,
                after=after,
                before=before,
                limit=limit,
            ),
            auth=True,
        )

    async def fetch_order_fills(
            self: 'BaseClient',
            symbol: str,
            order_id: str | None = None,
            after: str | None = None,
            before: str | None = None,
            limit: int | None = None,
    ) -> list[dict]:
        """
        Fetch order fills transaction details
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/fills',
            json=OrderFillsParams(
                symbol=symbol,
                order_id=order_id,
                after=after,
                before=before,
                limit=limit,
            ),
            auth=True,
        )

    async def create_order_plan(
            self: 'BaseClient',
            symbol: str,
            side: Side,
            size: float,
            order_type: OrderType,
            trigger_type: TriggerType,
            trigger_price: float,
            execute_price: float | None = None,
            client_oid: str | None = None,
            time_in_force_value: str | None = None,
    ) -> dict:
        """
        Create order plan
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/placePlan',
            json=OrderPlanCreateParams(
                symbol=symbol,
                side=side,
                size=size,
                order_type=order_type,
                trigger_type=trigger_type,
                trigger_price=trigger_price,
                execute_price=execute_price,
                client_oid=client_oid,
                time_in_force_value=time_in_force_value,
            ),
            auth=True,
        )

    async def update_order_plan(
            self: 'BaseClient',
            order_id: str,
            order_type: OrderType,
            trigger_price: float,
            execute_price: float | None = None,
            size: str | None = None,
    ) -> dict:
        """
        Update order plan
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/modifyPlan',
            json=OrderPlanUpdateParams(
                order_id=order_id,
                order_type=order_type,
                trigger_price=trigger_price,
                execute_price=execute_price,
                size=size,
            ),
            auth=True,
        )

    async def cancel_order_plan(
            self: 'BaseClient',
            order_id: str,
    ) -> int:
        """
        Cancel order plan
        """
        result = await self.post(
            url=SPOT_TRADE_PATH + '/cancelPlan',
            json=OrderPlanCancelParams(
                order_id=order_id,
            ),
            auth=True,
        )

        return int(result)

    async def fetch_current_order_plan(
            self: 'BaseClient',
            symbol: str,
            page_size: str | None = None,
            last_end_id: str | None = None,
    ) -> dict:
        """
        Fetch current order plan
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/currentPlan',
            json=OrderPlanParams(
                symbol=symbol,
                page_size=page_size,
                last_end_id=last_end_id,
            ),
            auth=True,
        )

    async def fetch_history_order_plan(
            self: 'BaseClient',
            symbol: str,
            start_time: str,
            end_time: str,
            page_size: str,
            last_end_id: str | None = None,
    ) -> dict:
        """
        Fetch history order plan
        """
        return await self.post(
            url=SPOT_TRADE_PATH + '/historyPlan',
            json=HistoryOrderPlanParams(
                symbol=symbol,
                start_time=start_time,
                end_time=end_time,
                page_size=page_size,
                last_end_id=last_end_id,
            ),
            auth=True,
        )
