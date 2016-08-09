from flask import Flask, g
from flask.ext.restful import Resource, fields, reqparse, marshal
from app.server.Models import ModelFactory
from app.server.Models.Authentication import auth
from app import db

from flask import url_for

user_fields = {
    'email': fields.String,
    'url': fields.Url('user')
}

'''Shows a list of all users, and lets you Create a new user'''
class UserListAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        ############ Add Arguments of the Web Request #################
        self.reqparse.add_argument("email", type = str, required = True, help = 'No email provided', location = 'json')
        self.reqparse.add_argument("password", type = str, required = True, help = 'No passoword provided', location = 'json')
        super(UserListAPI, self).__init__()
    
    '''Security - For now any registered user can get the list of all users. TODO: Change this later '''
    def get(self):
        '''List all users'''
        return ({'users': marshal(db.users.get_all(), user_fields) })

    '''Security - Only a Superuser can create a new user'''
    def post(self):
        '''Create a new user'''
        print("In Post: Create User")
        args = self.reqparse.parse_args()
        print(args)
        if (g.user.is_superuser == True):
            return ({'users': marshal(db.users.create(args), user_fields) })
        return ({'status' : 'Forbidden Access'}), 403


class UserAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", type = str, required = True, help = 'No email provided', location = 'json')
        self.reqparse.add_argument("password", type = str, required = True, help = 'No passoword provided', location = 'json')
        super(UserAPI, self).__init__()

    '''Security - For now any registered user can get info on a user. TODO: Change this later '''
    def get(self, id):
        '''Fetch a given resource'''
        print("In Single user get")
        u = db.users.get_by_id(id)
        if not u:
            api.abort(404, "User {} doesn't exist".format(id))
        return ({'user': marshal(u, user_fields) })
        
    '''Security - Only an Admin can delete any user'''
    def delete(self, id):
        '''Delete a user given its identifier'''
        print("In Single user delete")
        if (g.user.is_admin == True):
            db.users.delete(id)
            return ({'status': 'Successs'}), 204
        else:
            return ({'status' : 'Forbidden Access'}), 403

    '''Security - Only a Superuser can update an user'''
    def put(self, id):
        '''Update a user given its identifier'''
        print("In Single user Update")
        args = self.reqparse.parse_args()
        print(args)
        if (g.user.is_superuser == True):
            return ({'user': marshal(db.users.update(id, args), user_fields) }), 201
        return ({'status' : 'Forbidden Access'}), 403
