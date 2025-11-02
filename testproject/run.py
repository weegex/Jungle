import asyncio
import sys
from jungle import setup
import settings


if __name__ == "__main__":
    try:
        ip_port = sys.argv[1].split(":")
        ip = ip_port[0]
        port = ip_port[1]
        asyncio.run(setup(ip, port, settings.PROJECT_NAME))
    except IndexError:
        asyncio.run(setup(project_name=settings.PROJECT_NAME))
