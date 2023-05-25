# UUID
import datetime
import uuid

# Flask
from flask_restful import Resource, abort, request, output_json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_apispec import marshal_with, doc, use_kwargs, Ref
from flask_apispec.views import MethodResource

# Extensions
from src.extensions.database import db, pagination
from src.extensions.cache import cache

# Schemas
from src.shemas.schemas import UserCreateSchema, UserReadSchema, UserUpdateSchema

# Models
from src.models.models import User


# Verify Token
from src.api.security.token_provider import verify_token, create_token_jwt


# Helpers

user_create = UserCreateSchema()
user_read = UserReadSchema()
user_update = UserUpdateSchema()


# Create User
class CreateUser(MethodResource, Resource):

    #@verify_token
    @doc(description='', tags=['Users'])
    @use_kwargs(UserCreateSchema, location=('json'))
    @marshal_with(UserReadSchema)  # marshalling
    def post(self, **kwargs):

        user = User(**kwargs)
        user.uuid = uuid.uuid4().hex
        user.password = generate_password_hash(user.password, method='sha256')
        user.created_at = datetime.datetime.now()
        user.updated_at  = datetime.datetime.now()

        db.session.add(user)
        db.session.commit()

        rs = user_read.dump(user)
        response = {
            "user": rs
        }

        return output_json(response, 201)


# Get All Users
class GetAllUsers(MethodResource, Resource):

    #@verify_token
    @doc(description='', tags=['Users'])
    @marshal_with(UserReadSchema)
    @cache.cached(timeout=20, query_string=True)
    def get(self):
        users = pagination.paginate(User.query.all() or abort(404), schema=UserReadSchema(), marshmallow=True)
        rs = user_read.load(users['data'], many=True)
        response = {
            "users": rs,
            "pagination": users["pagination"]
        }
        return output_json(response, 200)


# Get One User
class GetOneUser(MethodResource, Resource):

    #@verify_token
    @doc(description='', tags=['Users'])
    @marshal_with(UserReadSchema)
    @cache.cached(timeout=120, query_string=True)
    def get(self, uuid):
        user = User.query.filter_by(uuid=uuid).first() or abort(404)
        rs = user_read.dump(user)
        response = {
            "user": rs
        }

        return output_json(response, 200)


# Update User
class UpdateUser(MethodResource, Resource):

    #@verify_token
    @doc(description='', tags=['Users'])
    @use_kwargs(UserUpdateSchema, location=('json'))
    @marshal_with(UserReadSchema)
    @cache.cached(timeout=120, query_string=True)
    def patch(self, uuid, **kwargs):
        user = User.query.filter_by(uuid=uuid).first() or abort(404)

        for k, v in kwargs.items():
            if v is not None:
                setattr(user, k, v)
        db.session.add(user)
        db.session.commit()

        rs = user_read.dump(user)

        response = {
            "user": rs
        }
        return output_json(response, 200)


class DeleteUser(MethodResource, Resource):

    @doc(description="", tags=['Users'])
    def delete(self, uuid):
        user = User.query.filter_by(uuid=uuid).first() or abort(404)

        db.session.delete(user)
        db.session.commit()

        response = {
            "message": "User deleted success"
        }
        return output_json(response, 200)


# Login User
class LoginUser(MethodResource, Resource):
    def post(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {'message': 'E-mail ou senha são obrigatórios'}, 401, {'WWW-Authenticate': 'Basic realm="Login requerido"'}
        user = User.query.filter_by(email=auth.username).first()
        if not user:
            return {'message': 'E-mail não existe'}, 401, {'WWW-Authenticate': 'Basic realm="Login requerido"'}
        if check_password_hash(user.password, auth.password):
            token = create_token_jwt(user.uuid)
            return {'message': 'Token gerado com sucesso'}, 200, {'Access-Token': str(token)}
        return {'message': 'E-mail ou senha incorretos'}, 401, {'WWW-Authenticate': 'Basic realm="Login requerido"'}
