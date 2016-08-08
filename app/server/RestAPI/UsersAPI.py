from flask import Flask
from flask.ext.restful import Resource, fields, reqparse, marshal
from app.server.Models import ModelFactory, db

from flask import url_for

user_fields = {
    'email': fields.String,
    'url': fields.Url('user')
}

class UserListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        ############ Add Arguments of the Web Request #################
        self.reqparse.add_argument("email", type = str, required = True, help = 'No email provided', location = 'json')
        self.reqparse.add_argument("password", type = str, required = True, help = 'No passoword provided', location = 'json')
        super(UserListAPI, self).__init__()
    
    '''Shows a list of all users, and lets you Create a new user'''
    def get(self):
        '''List all users'''
        return ({'users': marshal(db.users.get_all(), user_fields) })

    def post(self):
        '''Create a new user'''
        print("In Post: Create User")
        args = self.reqparse.parse_args()
        print(args)
        return ({'users': marshal(db.users.create(args), user_fields) })


class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", type = str, required = True, help = 'No email provided', location = 'json')
        self.reqparse.add_argument("password", type = str, required = True, help = 'No passoword provided', location = 'json')
        super(UserAPI, self).__init__()

    '''Show a single user item'''
    def get(self, id):
        '''Fetch a given resource'''
        print("In Single user get")
        u = db.users.get_by_id(id)
        if not u:
            api.abort(404, "User {} doesn't exist".format(id))
        return ({'user': marshal(u, user_fields) })
        

    def delete(self, id):
        '''Delete a user given its identifier'''
        print("In Single user delete")
        db.users.delete(id)
        return ({'status': 'Successs'}), 204

    def put(self, id):
        '''Update a user given its identifier'''
        print("In Single user Update")
        args = self.reqparse.parse_args()
        print(args)
        return ({'user': marshal(db.users.update(id, args), user_fields) }), 201
