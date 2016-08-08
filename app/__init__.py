from flask import Flask, render_template
from flask.ext.restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
from app.server.WebPages import views
from app.server.RestAPI.SparksAPI import SparkListAPI, SparkAPI
from app.server.RestAPI.UsersAPI import UserListAPI, UserAPI

# Register Spark REST API
api.add_resource(SparkListAPI, '/sparks', endpoint = 'sparks')
api.add_resource(SparkAPI, '/sparks/<int:id>', endpoint = 'spark')

# Register User REST API
api.add_resource(UserListAPI, '/users', endpoint = 'users')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')

from assets import assets