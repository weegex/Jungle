import asyncio
from jungle import tools
from dataclasses import dataclass


@dataclass
class RequestData:
    protocol: dict
    headers: dict
    content: str


async def path(*args, url, view, name=None):
    return (url, view, name)


class ASGIApp:

    def __init__(self, server, project_name) -> None:
        self.server = server
        self.project_name = project_name

    async def handler(self, receive, send):
        self.receive = receive
        self.send = send
        self.request = await self.check()
        method = self.request.protocol["method"]
        type = self.request.protocol["type"]
        host = tools.concatinate(
            str(send.get_extra_info("sockname")[0]),
            str(send.get_extra_info("sockname")[1]),
            separator=":"
        )
        url = host + self.request.protocol["suburl"]
        if type.startswith("HTTP"):
            url = "http://" + url

        tools.timed_print(
            tools.style("Receive", "yellow dim"),
            tools.style(type, "dim"),
            method,
            url
        )

        await self.run_view()

    async def check(self):
        request = bytearray()
        chunk = await self.receive.read(1024)
        request += chunk
        return await self.convert_headers(request.decode())

    async def convert_headers(self, request):
        converted_request = {}

        method = request.split("\n", 1)[0].split()
        converted_request["protocol"] = {}
        converted_request["protocol"]["method"] = method[0]
        converted_request["protocol"]["suburl"] = method[1]
        converted_request["protocol"]["type"] = method[2]

        ch = request.split("\r\n\r\n", 1)

        headers = ch[0].split("\r\n")[1:]
        content = ch[1]

        converted_request["headers"] = {}

        for header in headers:
            header = header.split(":", 1)
            header_name = header[0].lower()
            header_content = header[1].lstrip()

            converted_request["headers"][header_name] = header_content

        converted_request["content"] = content

        request = RequestData(
            converted_request["protocol"],
            converted_request["headers"],
            converted_request["content"]
        )

        return request

    async def run_view(self):
        urls = __import__(str(self.project_name) + ".urls")

        urls = urls.pattern()
        tools.log(urls)
