from aiohttp import web
from models.user import User as UserModel
from services.user import User as UserService

class User:
    def __init_(self):
        pass

    async def create(self, request):
        try:
            data = await request.json()
            UserService.create(data=data)
            return web.json_response(data, status=201)
        except:
            return web.HTTPBadRequest()
    
    async def login(self, request):
        try:
            data = await request.json()
            user = await UserService.login(data)
            return web.json_response(user, status=200)
        except UserModel.DoesNotExist:
            user = None
            return web.HTTPUnauthorized()
        except Exception:
            return web.HTTPBadRequest()
        

       
 