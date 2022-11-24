import logging
import sys
import time
from aiohttp import web
from models.base_model import database

from resources.user import User as UserResource
from resources.post import  Post as PostResource

from models.user import User as UserModel
from models.post import Post as PostModel
from models.post_request_info import PostRequestInfo as PostRequestInfoModel

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == '__main__':
    time.sleep(5)
    database.create_tables([UserModel, PostRequestInfoModel, PostModel])

    host = sys.argv[1]
    port = sys.argv[2]

    logging.info(f'Iniciando Servidor {host}:{port}')
    
    app = web.Application()
    userResource = UserResource()
    postResource = PostResource()
    app.add_routes(
        [
            web.post('/user', userResource.create),
            web.post('/login', userResource.login),
            web.post('/post', postResource.create),
            web.post('/post/add_spam', postResource.add_spam),
            web.post('/post/remove_spam', postResource.remove_spam),
            web.get('/post', postResource.list),
            web.get('/post/spam', postResource.list_spam),
            web.get('/', postResource.handle_intro)
        ]
    )
    web.run_app(app, host=host, port=port)
   