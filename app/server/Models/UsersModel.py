from app.server.Models.User import User
from app.server.Models.Authentication import auth

class UsersModel(object):
    def __init__(self):
        self.counter = 0
        self.users = []

    def get_all(self):
        return self.users;

    def get_by_id(self, id):
        print("In get User" + str(id))
        for user in self.users:
            if user.get_id() == id:
                return user
        return None

    def get_by_email(self, email):
        print("In get User" + str(id))
        for user in self.users:
            if user.get_email() == email:
                return user
        return None

    def create(self, data):
        print ("In UsersModel.create")
        user = User(self.counter, data['email'], data['password'])
        self.counter = self.counter + 1
        self.users.append(user)
        return user

    def update(self, id, data):
        user = self.get(id)
        user.update(data)
        return user

    def delete(self, id):
        user = self.get(id)
        self.users.remove(user)
