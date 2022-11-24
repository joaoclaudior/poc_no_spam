from peewee import *

from models.base_model import BaseModel

class PostRequestInfo(BaseModel):
    id = AutoField()
    user_ip = CharField()
    user_agent = CharField()