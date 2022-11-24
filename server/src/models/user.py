from peewee import *
import peewee_async

from models.base_model import BaseModel

class User(BaseModel):
    id = AutoField()
    name = CharField()
    email = CharField()
    password = CharField()
    delete = BooleanField(default=False)
    blocked = BooleanField(default=False)
    role = CharField(default='user')