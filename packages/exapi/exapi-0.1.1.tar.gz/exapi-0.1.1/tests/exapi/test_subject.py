import anyio

from exapi import Subject


async def main():
    subject = Subject()

    async def sender(stream):
        await anyio.sleep(0)
        for i in range(5):
            stream.next(i)
        subject.complete()

    async def printer(stream, n):
        async for item in stream:
            print(f'printer_{n} = {item}')
            await anyio.sleep(n)

    async with anyio.create_task_group() as task_group:
        task_group.start_soon(printer, subject, 1)
        task_group.start_soon(printer, subject, 2)
        task_group.start_soon(sender, subject)
        task_group.start_soon(printer, subject, 3)


if __name__ == '__main__':
    try:
        anyio.run(main, backend='asyncio', backend_options={'use_uvloop': True})
    except KeyboardInterrupt:
        pass
