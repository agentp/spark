from flask import Flask, render_template
from flask.ext.restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


from app.server.Models import ModelFactory
from app.server.WebPages import views

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
    'password' : 'simple1',
    'is_su' : False,
    'is_admin' : False,
    'is_theone': False
})

db.users.create({
    'email': 'ssd1@vdfg.com',
    'password' : 'simple2',
    'is_su' : False,
    'is_admin' : False,
    'is_theone': False
})

db.users.create({
    'email': 'ssd2@vdfg.com',
    'password' : 'simple2',
    'is_su' : False,
    'is_admin' : False,
    'is_theone': False
})

db.users.create({
    'email': 'admin@sparc.com',
    'password' : 'simple2',
    'is_su' : True,
    'is_admin' : True,
    'is_theone': False
})

db.users.create({
    'email': 'creator@sparc.com',
    'password' : 'create',
    'is_su' : True,
    'is_admin' : False,
    'is_theone': False
})

db.users.create({
    'email': 'hulk@sparc.com',
    'password' : 'create',
    'is_su' : True,
    'is_admin' : True,
    'is_theone': True
})


from app.server.RestAPI.SparksAPI import SparkListAPI, SparkAPI
from app.server.RestAPI.UsersAPI import UserListAPI, UserAPI

# Register Spark REST API
api.add_resource(SparkListAPI, '/sparks', endpoint = 'sparks')
api.add_resource(SparkAPI, '/sparks/<int:id>', endpoint = 'spark')

# Register User REST API
api.add_resource(UserListAPI, '/users', endpoint = 'users')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')


from assets import assets