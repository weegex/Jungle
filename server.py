import asyncio


class Server:
    """Async server"""

    def __init__(self, ip, port) -> None:
        """__init__ class Server

        Args:
            ip (str): ip address for server
            port (_type_): port for server
        """
        self.ip = ip
        self.port = port

    async def run(self, asgi):
        """def for run the server

        Args:
            asgi (class): ASGI main app
        """
        self.server = await asyncio.start_server(asgi, self.ip, self.port)
        await self.server.serve_forever()
