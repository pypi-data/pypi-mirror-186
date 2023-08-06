from asyncio import Future, sleep


class Subject:

    def __init__(self):
        self.waiter = Future()

    def complete(self):
        if not self.waiter.cancelled():
            self.waiter.set_result((None, None))

    def next(self, value):
        waiter, self.waiter = self.waiter, Future()
        waiter.set_result((value, self.waiter))

    async def subscribe(self):
        waiter = self.waiter
        while True:
            value, waiter = await waiter
            if waiter is None:
                break
            yield value
            await sleep(0)

    __aiter__ = subscribe
