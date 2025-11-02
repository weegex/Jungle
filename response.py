import asyncio
from jungle import tools
from jungle.config import *


class Response:
    def __init__(self, body, status, description="", type="TEXT") -> None:
        self.body = body
        self.status = status
        self.description = description
        self.type = type

    async def __call__(self, send):
        host = tools.concatinate(
            str(send.get_extra_info("sockname")[0]),
            str(send.get_extra_info("sockname")[1]),
            separator=":"
        )
        url = host + self.request.protocol["suburl"]
        if type.startswith("HTTP"):
            url = "http://" + url

        if str(self.status).startswith("1"):
            status = tools.style(self.status, "cyan")
        elif str(self.status).startswith("2"):
            status = tools.style(self.status, "bright green")
        elif str(self.status).startswith("3"):
            status = tools.style(self.status, "yellow")
        elif str(self.status).startswith("4"):
            status = tools.style(self.status, "bright red")
        elif str(self.status).startswith("5"):
            status = tools.style(self.status, "bright red")

        if not self.description:
            if self.status == 200:
                description = "OK"
            elif self.status == 302:
                description = "Found"
            elif self.status == 400:
                description = "Bad Request"
            elif self.status == 403:
                description = "Forbidden"
            elif self.status == 404:
                description = "Not Found"
            elif self.status == 500:
                description = "Internal Error"
        else:
            description = self.description

        if self.type == "HTML":
            type = "text/html"
        elif self.type == "TEXT":
            type = "text/plain"
        elif self.type == "CSS":
            type = "text/css"
        elif self.type == "JS":
            type = "text/javascript"

        send.send(
            tools.concatinate(
                tools.concatinate(
                    self.request.protocol["type"],
                    status,
                    description
                ),
                tools.concatinate(
                    "Server:",
                    NAME,
                    VERSION
                ),
                tools.concatinate(
                    "content-type:",
                    str(type)
                ),
                tools.concatinate(
                    "host:",
                    host
                ),
                tools.concatinate(
                    "\n",
                    self.body
                ),
                separator="\r\n"
            ).encode()
        )

        tools.timed_print(
            tools.style("Answer", "yellow dim"),
            tools.style(self.request.protocol["type"], "dim"),
            status,
            url
        )


class HttpResponse:
    def __init__(self, html, status, description=None) -> None:
        self.html = html
        self.status = status
        self.description = description

    async def __call__(self, request, send):
        response = Response(self.html, self.status, self.description, "TEXT")
        response(send)
