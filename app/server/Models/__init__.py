from app.server.Models.SparksModel import SparksModel

class ModelFactory(object):
    def __init__(self):
        self.sparks = SparksModel()

    def GetSparkModel(self):
        return self.sparks




db = ModelFactory()

########################### Test ####################################################
db.sparks.create({
    'title': 'My Great Idea', 
    'body': "sfsgddfgfdg", 
    'messages': [
        {
            'id': 1,
            'body': 'Hello'
        },
        {
            'id': 2,
            'body': 'World'
        }
    ] 
})

db.sparks.create({
    'title': 'Really good Idea', 
    'body': "sfsgddfgfdg", 
    'messages': [
        {
            'id': 1,
            'body': 'Hello'
        },
        {
            'id': 2,
            'body': 'World'
        }
    ] 
})

db.sparks.create({
    'title': 'Really yuge Idea', 
    'body': "sfsgddfgfdg", 
    'messages': [
        {
            'id': 1,
            'body': 'Hello'
        },
        {
            'id': 2,
            'body': 'World'
        }
    ] 
})

##############################################################################################