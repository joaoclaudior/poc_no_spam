from models.user import User as UserModel
from playhouse.shortcuts import model_to_dict

class User:
    def __init__(self):
        pass

    @staticmethod
    def create(data):
        if 'name' in data and data['name']:
            name = data['name']
        if 'email' in data and data['email']:
            email = data['email']
        if 'password' in data and data['password']:
            password = data['password']
        if not name or not email or not password:
            raise Exception("Dados Invalidos")
        user = UserModel(name=name, email=email, password=password)
        user.save()
    
    @staticmethod
    async def login(data):
        email = ''
        password = ''
        if 'email' in data and data['email']:
            email = data['email']
        if 'password' in data and data['password']:
            password = data['password']
        if not email or not password:
            raise Exception("Dados Invalidos")

        user = await UserModel.manege.get(UserModel, email=email, password=password, delete=False, blocked=False)
        user_dict = model_to_dict(user)
        del user_dict['password']
        return user_dict