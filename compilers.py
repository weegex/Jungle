import asyncio


class AppsCompiler():
    def __init__(self, request, receive, send) -> None:
        self.request = request
        self.receive = receive
        self.send = send

    async def run(self):
        pass
