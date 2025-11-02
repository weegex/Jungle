import apps.test.views as views


async def pattern(path):
    return [
        await path("main1/", view=views.Main)
    ]
