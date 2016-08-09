from flask import Flask, jsonify, g
from flask.ext.httpauth import HTTPBasicAuth
from app.server.Models.User import User
from app import app, db

auth = HTTPBasicAuth()

@app.route('/auth/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(secret=app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('ascii') })

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token, db.users, secret=app.config['SECRET_KEY'])
    if not user:
        # try to authenticate with username/password
        user = db.users.get_by_email(username_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True