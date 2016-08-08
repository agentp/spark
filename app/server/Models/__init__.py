
from app.server.Models.SparksModel import SparksModel
from app.server.Models.UsersModel import UsersModel
from app.server.Models.User import User

class ModelFactory(object):
    def __init__(self):
        self.sparks = SparksModel()
        self.users = UsersModel()

    def GetSparkModel(self):
        return self.sparks

    def GetUsersModel(self):
        return self.users

db = ModelFactory()

########################### Test ####################################################
db.sparks.create({
    'title': 'My Great Idea', 
    'body': "sfsgddfgfdg",
    'fires' : [1,2],
    'owner' : 1
})

db.sparks.create({
    'title': 'Really good Idea', 
    'body': "sfsgddfgfdg",
    'fires' : [1,2],
    'owner' : 1
})


db.users.create({
    'email': 'ssd1@vdfg.com',
    'password' : 'simple1'
})

db.users.create({
    'email': 'ssd1@vdfg.com',
    'password' : 'simple2'
})

db.users.create({
    'email': 'ssd2@vdfg.com',
    'password' : 'simple2'
})
