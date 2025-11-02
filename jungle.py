from jungle.server import Server
from jungle.asgi import ASGIApp
import asyncio
import os


async def setup(ip: str = "127.0.0.1", port: int = 8000, project_name: str = ""):
    server = Server(ip, port)
    await server.run(ASGIApp(server, project_name).handler)


if __name__ == "__main__":
    asyncio.run(setup())
