from akismet import Akismet
from models.post import Post
import os

AKISMET_API_KEY=os.environ.get('AKISMET_API_KEY','')
AKISMET_BLOG_URL=os.environ.get('AKISMET_BLOG_URL', '')

class Akimets:
    @staticmethod
    async def check_is_spam(post: Post):
        akismet_api = Akismet(key=AKISMET_API_KEY, blog_url=AKISMET_BLOG_URL)
        is_spam = akismet_api.comment_check(
            user_agent=post.info_request.user_agent,
            user_ip=post.info_request.user_ip,
            comment_type='forum-post',
            comment_author=post.user.name,
            comment_author_email=post.user.email,
            comment_content=post.post,
            blog_charset='UTF-8',
            blog_lang='pt',
            user_role=post.user.role
        )
        return is_spam
    
    @staticmethod
    async def submit_spam(post: Post):
        akismet_api = Akismet(key=AKISMET_API_KEY, blog_url=AKISMET_BLOG_URL)
        akismet_api.submit_spam(
            user_agent=post.info_request.user_agent,
            user_ip=post.info_request.user_ip,
            comment_type='forum-post',
            comment_author=post.user.name,
            comment_author_email=post.user.email,
            comment_content=post.post,
            blog_charset='UTF-8',
            blog_lang='pt',
            user_role=post.user.role
        )
    
    @staticmethod
    async def submit_ham(post: Post):
        akismet_api = Akismet(key=AKISMET_API_KEY, blog_url=AKISMET_BLOG_URL)
        akismet_api.submit_ham(
            user_agent=post.info_request.user_agent,
            user_ip=post.info_request.user_ip,
            comment_type='forum-post',
            comment_author=post.user.name,
            comment_author_email=post.user.email,
            comment_content=post.post,
            blog_charset='UTF-8',
            blog_lang='pt',
            user_role=post.user.role
        )
