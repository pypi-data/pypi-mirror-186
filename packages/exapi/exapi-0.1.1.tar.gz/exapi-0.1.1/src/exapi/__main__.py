import anyio


async def main():
    pass


if __name__ == '__main__':
    try:
        anyio.run(main, backend='asyncio', backend_options={'use_uvloop': True})
    except KeyboardInterrupt:
        pass
