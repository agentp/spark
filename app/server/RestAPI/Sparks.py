from flask import Flask
from flask_restplus import Resource, Api
from app import app
from app import api

################## Test Data (Model) ################### 
####### Convert to Database access Later #######

class SparkDb(object):
    def __init__(self):
        self.counter = 0
        self.sparks = []

    def get(self, id):
        for spark in self.sparks:
            if spark['id'] == id:
                return spark
        api.abort(404, "Spark {} doesn't exist".format(id))

    def create(self, data):
        spark = data
        spark['id'] = self.counter = self.counter + 1
        self.sparks.append(spark)
        return spark

    def update(self, id, data):
        spark = self.get(id)
        spark.update(data)
        return spark

    def delete(self, id):
        spark = self.get(id)
        self.sparks.remove(spark)

class DataBase(object):
    def __init__(self):
        self.sparks = SparkDb()

    def GetSparkDb(self):
        return self.sparks


db = DataBase()
db.sparks.create({'spark': 'My Great Idea'})
db.sparks.create({'spark': 'Really good Idea'})
db.sparks.create({'spark': 'Really yuge Idea'})

##############################################################################################


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
    'flame_list_id': fields.Integer(required=True, description='The Flames to which this spark is assigned'),
    'title': fields.String(required=True, description='The Title of the spark'),
    'body': fields.String(required=True, description='The Body of the spark'),
    'message_list_id': fields.Integer(required=True, description='List of messages'),
    'user_id': fields.Integer(required=True, description='Owner of this idea'),
    'rouse_user_list_id':  fields.Integer(required=True, description='List of users who admired the ideas and want it to grow'),
    'douse_user_list_id':  fields.Integer(required=True, description='List of users who despise the ideas'),
    'reignite_user_list_id':  fields.Integer(required=True, description='List of users who suggest it to their Tribes')
})

@ns.route('/')
class SparksList(Resource):
    '''Shows a list of all sparks, and lets you POST to add new sparks'''
    @ns.doc('list_sparks')
    @ns.marshal_list_with(spark)
    def get(self):
        '''List all sparks'''
        return db.sparks

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
