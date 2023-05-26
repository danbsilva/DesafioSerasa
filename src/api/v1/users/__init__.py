from flask import Blueprint
from flask_restful import Api

from src.extensions.csrf import csrf
from src.extensions.swagger import docs

from src.api.v1.users.user_resources import *

from src.api.v1 import __prefix__

bp_users = Blueprint('users', __name__, url_prefix=__prefix__ + '/users')
api = Api(bp_users, decorators=[csrf.exempt])


def init_app(app):
    app.register_blueprint(bp_users)

    api.add_resource(CreateUser, "/")
    api.add_resource(GetAllUsers, "/")
    api.add_resource(GetOneUser, "/<uuid>/")
    api.add_resource(UpdateUser, "/<uuid>/")
    api.add_resource(DeleteUser, "/<uuid>/")
    api.add_resource(AuthUser, "/auth/")

    docs.register(CreateUser, blueprint=bp_users.name)
    docs.register(GetAllUsers, blueprint=bp_users.name)
    docs.register(GetOneUser, blueprint=bp_users.name)
    docs.register(UpdateUser, blueprint=bp_users.name)
    docs.register(DeleteUser, blueprint=bp_users.name)
    docs.register(AuthUser, blueprint=bp_users.name)