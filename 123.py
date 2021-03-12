from aiohttp import web
import requests


routes = web.RouteTableDef()


@routes.get('/')
async def main(request):
    return web.Response(text="Hello, world")


async def RUB(request):
    return web.Response(text='рубль')


async def USD():
    pass


async def EUR():
    pass


async def amount():
    pass


app = web.Application()
app.add_routes([web.get('/', main),
                web.get('/RUB', RUB),
                web.get('/USD', USD),
                web.get('/EUR', EUR),
                web.get('/amount', amount)])
web.run_app(app)

