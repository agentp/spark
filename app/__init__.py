from flask import Flask, render_template
from flask_restplus import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
api = Api(app, version='1.0', title='Spark Server API', description='A simple Spark Management API')
from app.server.WebPages import views
from app.server.RestAPI.SparksAPI import SparksList
from assets import assets