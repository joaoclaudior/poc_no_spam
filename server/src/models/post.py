import datetime
from peewee import *

from models.base_model import BaseModel
from models.post_request_info import PostRequestInfo
from models.user import User

class Post(BaseModel):
    id = AutoField()
    post = CharField()
    date_post = DateTimeField(default=datetime.datetime.now) 
    info_request = ForeignKeyField(PostRequestInfo)
    user = ForeignKeyField(User)
    delete = BooleanField(default=False)
    is_spam = BooleanField(default=False)