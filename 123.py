from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def main(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes(routes)
web.run_app(app)

