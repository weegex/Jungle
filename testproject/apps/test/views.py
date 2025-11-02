from jungle.response import HttpResponse
from jungle.views import View


class Main(View):
    async def run(self):
        return HttpResponse("test", 200, "OK")
