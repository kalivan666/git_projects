from aiohttp import web


async def main(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes([web.get('/', main)])
web.run_app(app)
