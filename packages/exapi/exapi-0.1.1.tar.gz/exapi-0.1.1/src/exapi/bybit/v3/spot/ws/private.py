from exapi import Subject
from exapi.bybit.v3 import BaseWebSocket


class PrivateWebSocket(BaseWebSocket):

    async def outbound_account_info_stream(self) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-outboundaccountinfo
        """
        return await self.subscribe(
            topic='outboundAccountInfo',
        )

    async def order_stream(self) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websocketspotorder
        """
        return await self.subscribe(
            topic='order',
        )

    async def stop_order_stream(self) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-websocketspotstoporder
        """
        return await self.subscribe(
            topic='stopOrder',
        )

    async def ticket_info_stream(self) -> Subject:
        """
        https://bybit-exchange.github.io/docs/spot/v3/#t-ticketinfo
        """
        return await self.subscribe(
            topic='ticketInfo',
        )
