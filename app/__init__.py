from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('config')
from app.server.HelloWorld import views
from assets import assets