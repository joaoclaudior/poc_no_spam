from aiohttp import web
from services.post import Post as PostService, SpamException


from utils.json import json_response

class Post:
    def __init_(self):
        pass
    
    async def create(self, request):
        try:
            data = await request.json()
            headers = request.headers
            user_agent = headers['User-Agent']
            user_ip = request.remote

            data = await PostService.create(data=data, user_agent=user_agent, user_ip=user_ip)
    
            return json_response(data, status=201)
        except SpamException as error:
            return web.HTTPForbidden(text=str(error))
        except Exception:
            return web.HTTPBadRequest()
    
    async def list(self, request):
        try:
            posts = await PostService.list()
            return json_response(posts, status=200)
        except:
            return web.HTTPBadRequest()

    async def list_spam(self, request):
        try:
            posts = await PostService.list(is_spam=True)
            return json_response(posts, status=200)
        except:
            return web.HTTPBadRequest()
    
    async def add_spam(self, request):
        # try:
            data = await request.json()
            await PostService.add_spam(data)
            return json_response(data, status=200)
        # except:
            return web.HTTPBadRequest()
    
    async def remove_spam(self, request):
        try:
            data = await request.json()
            await PostService.remove_spam(data)
            return json_response(data, status=200)
        except:
            return web.HTTPBadRequest()

    async def handle_intro(self, request):
        return web.Response(text="Hello, world")

