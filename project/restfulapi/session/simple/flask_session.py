from flask import jsonify, request
import flask_restful
from flask_login import login_required, login_user, logout_user, UserMixin
from project.restfulapi import blueprints

api = flask_restful.Api(blueprints[__package__], prefix="/session")


#This should be in Models
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return str(self.id)
        

@api.route('/')
class SimpleLogout(flask_restful.Resource):

    @login_required
    def delete(self):
        logout_user()
        return jsonify({'status': 'logout_ok',
                       'message': 'Log out from backend services was successful.'})


#Do not add a route for this class.
#Subclass it, and override the "validate" method.
class Login(flask_restful.Resource):

    def post(self):
        if self.validate(request.values):
            # Should get database user id from self.[properties]
            # And create new user if ID is not found.
            # It uses id=0 for all users.
            user = User(0)
            login_user(user)
            return jsonify({'status': 'login_ok',
                            'message': 'Log in to backend services was successful.'})
        else:
            response = jsonify({'status': 'login_failed'})
            response.status_code = 400
            return response
    
    def validate(self):
        return False