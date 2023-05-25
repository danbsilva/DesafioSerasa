from flask import Blueprint
from flask_restful import Api

from src.extensions.csrf import csrf
from src.extensions.swagger import docs

from src.api.v1.resources.user_resources import *

prefix = '/api/v1'

bp = Blueprint('v1', __name__, url_prefix=prefix)
api = Api(bp, decorators=[csrf.exempt])


def init_app(app):

    # Users
    api.add_resource(CreateUser, "/users/")
    api.add_resource(GetAllUsers, "/users/")
    api.add_resource(GetOneUser, "/users/<uuid>/")
    api.add_resource(UpdateUser, "/users/<uuid>/")
    api.add_resource(DeleteUser, "/users/<uuid>/")
    api.add_resource(LoginUser, "/users/login/")

    app.register_blueprint(bp)

    docs.register(CreateUser, blueprint=bp.name)
    docs.register(GetAllUsers, blueprint=bp.name)
    docs.register(GetOneUser, blueprint=bp.name)
    docs.register(UpdateUser, blueprint=bp.name)
    docs.register(DeleteUser, blueprint=bp.name)