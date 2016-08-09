from flask import Flask, g
from flask.ext.restful import Resource, fields, reqparse, marshal
from app.server.Models import ModelFactory
from app.server.Models.Authentication import auth
from app import db
from flask import url_for

spark_fields = {
    'title': fields.String,
    'body': fields.String,
    'url': fields.Url('spark')
}

class SparkListAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        ############ Add Arguments of the Web Request #################
        self.reqparse.add_argument("title", type = str, required = True, help = 'No task title provided', location = 'json')
        self.reqparse.add_argument("body", type = str, default = "", location = 'json')
        super(SparkListAPI, self).__init__()
    
    '''Shows a list of all sparks, and lets you POST to add new sparks'''
    def get(self):
        '''List all sparks'''
        return ({'sparks': marshal(db.sparks.get_all(), spark_fields) })

    def post(self):
        '''Create a new spark'''
        print("In Post: Create Spark")
        args = self.reqparse.parse_args()
        print(args)
        return ({'sparks': marshal(db.sparks.create(args), spark_fields) })


class SparkAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('body', type = str, location = 'json')
        super(SparkAPI, self).__init__()

    '''Show a single spark item and lets you delete them'''
    def get(self, id):
        '''Fetch a given resource'''
        print("In Single Spark get")
        return ({'spark': marshal(db.sparks.get(id), spark_fields) })
        

    def delete(self, id):
        '''Delete a spark given its identifier'''
        print("In Single Spark delete")
        db.sparks.delete(id)
        return ({'status': 'Successs'}), 204

    def put(self, id):
        '''Update a spark given its identifier'''
        print("In Single Spark Update")
        args = self.reqparse.parse_args()
        print(args)
        return ({'spark': marshal(db.sparks.update(id, args), spark_fields) }), 201

