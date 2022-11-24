from playhouse.shortcuts import model_to_dict
from models.user import User as UserModel
from models.post_request_info import PostRequestInfo as PostRequestInfoModel
from models.post import Post as PostModel
from clients.akimets import Akimets

class Post:
    def __init__(self):
        pass

    @staticmethod
    async def create(data, user_ip, user_agent):
        comment_type='contact-form'
        post = ''
        user_id = ''

        if 'post' in data and data['post']:
            post = data['post']
        if 'user_id' in data and data['user_id']:
            user_id = data['user_id']
        if not post or not user_id:
            raise Exception("Dados Invalidos")
        
        user = await UserModel.manege.get(UserModel, id = user_id)
        pot_request_info = PostRequestInfoModel.create(user_ip=user_ip, user_agent=user_agent)
        post = PostModel(post=post, user=user, info_request=pot_request_info)
        is_spam = await Akimets.check_is_spam(post)
        post.is_spam = is_spam
        post.save()

        if is_spam:
            raise SpamException('Sua mensagem é um spam!!!')
        
        data_create = {
            'host': user_ip,
            'comment_type': comment_type,
            'user_agent': user_agent,
            'post': post.post,
            'user_id': user_id
        }

        return data_create
    
    @staticmethod
    async def remove_spam(data):
        post_id = ''
        if 'post_id' in data and data['post_id']:
            post_id = data['post_id']
        if not post_id:
            raise Exception("Dados Invalidos")

        post = await PostModel.manege.get(PostModel, id = post_id)
        await Akimets.submit_ham(post)
        await Akimets.submit_spam(post)
        PostModel.update({PostModel.is_spam: False}).where(PostModel.id == post_id).execute()
    
    @staticmethod
    async def add_spam(data):
        post_id = ''
        if 'post_id' in data and data['post_id']:
            post_id = data['post_id']
        if not post_id:
            raise Exception("Dados Invalidos")

        post = await PostModel.manege.get(PostModel, id = post_id)
        await Akimets.submit_spam(post)
        PostModel.update({PostModel.is_spam: True}).where(PostModel.id == post_id).execute()
        
    

    
    @staticmethod
    async def list(is_spam=False):
        posts = await PostModel.manege.execute(PostModel.select().where(PostModel.is_spam == is_spam))
        posts = [model_to_dict(post) for post in posts]
        for post in posts:
            del post['user']['password']
        return posts

class SpamException(Exception):
    pass