from exapi.bitget.v1 import BaseClient
from exapi.bitget.v1.constants import SPOT_PUBLIC_PATH
from exapi.bitget.v1.spot.client.public.models import ProductParams


class Public:

    async def fetch_server_time(self: 'BaseClient') -> int:
        """
        Fetch server time.
        """
        return int(await self.get(url=SPOT_PUBLIC_PATH + '/time'))

    async def fetch_currencies(self: 'BaseClient') -> list[dict]:
        """
        Fetch all currencies
        """
        return await self.get(url=SPOT_PUBLIC_PATH + '/currencies')

    async def fetch_products(self: 'BaseClient') -> list[dict]:
        """
        Fetch all transaction pair information
        """
        return await self.get(url=SPOT_PUBLIC_PATH + '/products')

    async def fetch_product(
            self: 'BaseClient',
            symbol: str,
    ) -> dict:
        """
        Fetch single currency pair information according to the transaction pair
        """
        return await self.get(
            url=SPOT_PUBLIC_PATH + '/product',
            params=ProductParams(
                symbol=symbol,
            ),
        )
