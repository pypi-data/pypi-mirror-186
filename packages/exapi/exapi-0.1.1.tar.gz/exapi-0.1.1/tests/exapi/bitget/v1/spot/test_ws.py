import anyio
from anyio import create_task_group

from exapi.bitget.v1.constants import SPOT_WS_URL
from exapi.bitget.v1.models import Topic
from exapi.bitget.v1.spot import SpotWebSocket


async def main():
    async with create_task_group() as spot_group:
        async with SpotWebSocket(
                url=SPOT_WS_URL,
                api_key='bg_40840f348d8c6f508c2ee1a9bf12c963',
                api_secret='4f799c71e9d183a2654a2acc9515af2026d79820f7864e58e64c067ff5c5c3bc',
                api_passphrase='SpotTradeSecret',
        ) as ws:
            spot_group.start_soon(ws.forever)
            await ws.wait_connected()

            async with create_task_group() as task_group:
                async def printer(subject, n):
                    async for data in subject.subscribe():
                        print(f'{n}: {data}')

                btc_subject = await ws.subscribe(
                    topic=Topic(
                        inst_type='sp',
                        channel='ticker',
                        inst_id='BTCUSDT',
                    )
                )
                task_group.start_soon(printer, btc_subject, 'btc')

                eth_subject = await ws.subscribe(
                    topic=Topic(
                        inst_type='sp',
                        channel='ticker',
                        inst_id='ETHUSDT',
                    )
                )
                task_group.start_soon(printer, eth_subject, 'eth')

                await anyio.sleep(5)
                await ws.unsubscribe_all()
                await anyio.sleep(5)

                atom_subject = await ws.subscribe(
                    topic=Topic(
                        inst_type='sp',
                        channel='ticker',
                        inst_id='ATOMUSDT',
                    )
                )
                task_group.start_soon(printer, atom_subject, 'atom')
                await anyio.sleep(5)
                await ws.unsubscribe(
                    topic=Topic(
                        inst_type='sp',
                        channel='ticker',
                        inst_id='ATOMUSDT',
                    )
                )

                btc_subject = await ws.subscribe(
                    topic=Topic(
                        inst_type='sp',
                        channel='ticker',
                        inst_id='BTCUSDT',
                    )
                )
                task_group.start_soon(printer, btc_subject, 'btc2')

                await anyio.sleep(5)
                await ws.unsubscribe_all()
                await anyio.sleep(5)
                print('END')
                # await task_group.cancel_scope.cancel()

            print('All tasks finished!')


if __name__ == '__main__':
    try:
        anyio.run(main, backend='asyncio', backend_options={'use_uvloop': True})
    except KeyboardInterrupt:
        pass
