import anyio
import logging
from exapi.bybit.v3 import SpotWebSocket
from exapi.bybit.v3.constants import SPOT_WS_PRIVATE_URL, SPOT_WS_PUBLIC_URL

logging.basicConfig(
    format="%(message)s",
    level=logging.DEBUG,
)


async def main():
    async with anyio.create_task_group() as spot_group:
        async with SpotWebSocket(
                url=SPOT_WS_PUBLIC_URL,
                # url=SPOT_WS_PRIVATE_URL,
                # api_key='g0k5D7yaqwlRaiDv1v',
                # api_secret='DXXf0HmPrhSuYKka9p5Hhb8uKfzxH5qOoBgG',
        ) as ws:
            spot_group.start_soon(ws.forever)
            await ws.wait_connected()

            async with anyio.create_task_group() as task_group:
                async def printer(subject, n):
                    async for data in subject.subscribe():
                        print(f'{n}: {data}')

                btc_subject = await ws.depth_stream(
                    symbol='BTCUSDT',
                    depth=3,
                )
                task_group.start_soon(printer, btc_subject, 'btc')

                eth_subject = await ws.depth_stream(
                    symbol='ETHUSDT',
                    depth=3,
                )
                task_group.start_soon(printer, eth_subject, 'eth')

                await anyio.sleep(5)
                await ws.unsubscribe_all()
                await anyio.sleep(3)
                print('END')

            print('All tasks finished!')


if __name__ == '__main__':
    try:
        anyio.run(main, backend='asyncio', backend_options={'use_uvloop': True})
    except KeyboardInterrupt:
        pass
