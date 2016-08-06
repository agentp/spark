from flask import Flask
from flask_restplus import Resource, fields
from app import app
from app import api
from app.server.Models import ModelFactory, db

ns = api.namespace('sparks', description='All the brilliant sparks to light up the world')

message = api.model('message', {
    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    'body': fields.String(required=True, description='The Title of the spark'),
    'user_id': fields.Integer(required=True, description='Owner of this idea'),
    'rouse_user_list_id':  fields.Integer(required=True, description='List of users who admired the ideas and want it to grow'),
    'douse_user_list_id':  fields.Integer(required=True, description='List of users who despise the ideas')
})

spark = api.model('Spark', {
    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    #'flame_list_id': fields.Integer(required=True, description='The Flames to which this spark is assigned'),
    'title': fields.String(required=True, description='The Title of the spark'),
    'body': fields.String(required=True, description='The Body of the spark')
    #'message_list_id': fields.Integer(required=True, description='List of messages'),
    #'user_id': fields.Integer(required=True, description='Owner of this idea'),
    #'rouse_user_list_id':  fields.Integer(required=True, description='List of users who admired the ideas and want it to grow'),
    #'douse_user_list_id':  fields.Integer(required=True, description='List of users who despise the ideas'),
    #'reignite_user_list_id':  fields.Integer(required=True, description='List of users who suggest it to their Tribes')
})

@ns.route('/')
class SparksList(Resource):
    '''Shows a list of all sparks, and lets you POST to add new sparks'''
    @ns.doc('list_sparks')
    @ns.marshal_list_with(spark)
    def get(self):
        '''List all sparks'''
        print("In List Get")
        print(db.sparks.get_all())
        return db.sparks.get_all()

    @ns.doc('create_spark')
    @ns.expect(spark)
    @ns.marshal_with(spark, code=201)
    def post(self):
        '''Create a new spark'''
        return db.sparks.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Spark not found')
@ns.param('id', 'The spark identifier')
class Spark(Resource):
    '''Show a single spark item and lets you delete them'''
    @ns.doc('get_spark')
    @ns.marshal_with(spark)
    def get(self, id):
        '''Fetch a given resource'''
        print("In Single resource get")
        return db.sparks.get(id)

    @ns.doc('delete_spark')
    @ns.response(204, 'Spark deleted')
    def delete(self, id):
        '''Delete a spark given its identifier'''
        db.sparks.delete(id)
        return '', 204

    @ns.expect(spark)
    @ns.marshal_with(spark)
    def put(self, id):
        '''Update a spark given its identifier'''
        return db.sparks.update(id, api.payload)
