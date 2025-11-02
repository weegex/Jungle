import asyncio
from jungle.response import Render
from jungle.views import View


class Main(View):
    async def run(self):
        return Render("index.html", {"name": "TEST TEXT"})


class Test(View):
    async def run(self):
        return Render("index1.html")
