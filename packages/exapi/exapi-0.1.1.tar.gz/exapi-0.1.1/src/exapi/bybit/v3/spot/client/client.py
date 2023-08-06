from time import time

from exapi.bybit.v3.client import BaseClient
from exapi.bybit.v3.spot.client.private import Private
from exapi.bybit.v3.spot.client.public import Public


class SpotClient(BaseClient, Public, Private):

    async def sync_time(self) -> None:
        server_time = await self.fetch_server_time()
        timestamp = int(time() * 1000)
        if server_time['serverTime'] - self._recv_window <= timestamp < server_time['serverTime'] + 1000:
            return
        raise RuntimeError('Need update local time')
