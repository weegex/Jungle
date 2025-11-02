import asyncio


class View:
    def __init__(self) -> None:
        pass

    async def __call__(self, request, send):
        self.request = request
        self.send = send
        await self.run()
