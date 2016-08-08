
from flask_restplus import fields
from app import api

fire = api.model('Spark', {
    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    'sparks': fields.List(fields.Integer())
})

