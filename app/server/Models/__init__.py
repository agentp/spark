
from app.server.Models.SparksModel import SparksModel
from app.server.Models.UsersModel import UsersModel

class ModelFactory(object):
    def __init__(self):
        self.sparks = SparksModel()
        self.users = UsersModel()

    def GetSparkModel(self):
        return self.sparks

    def GetUsersModel(self):
        return self.users

