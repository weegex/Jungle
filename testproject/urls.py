import views
import asyncio


async def pattern(path):
    return [
        await path(url="main/", view=views.Main),
        await path(url="", include="apps.test.urls")
    ]
