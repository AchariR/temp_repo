from flask_login import LoginManager, UserMixin
from project import app

class User(UserMixin):

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return str(self.id)

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    return User(userid)

from . import flask_session