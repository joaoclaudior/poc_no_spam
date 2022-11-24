from peewee import *
import peewee_async

database = peewee_async.MySQLDatabase('poc', user='user', password='user',
                         host='db_poc', port=3306)

class BaseModel(Model):
    manege = peewee_async.Manager(database)
        
    class Meta:
        database = database

        