from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('config')
api = Api(app, version='1.0', title='Spark Server API', description='A simple Spark Management API')
from app.server.HelloWorld import views
from app.server.RestAPI.Idea import SparksList
from assets import assets