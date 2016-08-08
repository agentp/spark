
from flask_restplus import fields
from app import api

message = api.model('message', {
    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    'body': fields.String(required=True, description='The Title of the spark'),
    'owner': fields.Nested(fields.Integer()),
    'rouse_user_list':  fields.List(fields.Integer()),
    'douse_user_list':  fields.List(fields.Integer()),
})
