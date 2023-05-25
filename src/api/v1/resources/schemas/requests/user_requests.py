from flask_restful import reqparse
from marshmallow import Schema, fields


# POST
class UserPostSchema(Schema):
    nome = fields.String(required=True, description="Nome")
    email = fields.String(required=True, description="Email")
    password = fields.String(required=True, description="Password")


user_fields_post = reqparse.RequestParser()
user_fields_post.add_argument('uuid', type=str, location='json')
user_fields_post.add_argument('nome', type=str, required=True, location='json')
user_fields_post.add_argument('email', type=str, required=True, location='json')
user_fields_post.add_argument('password', type=str, required=True, location='json')


user_fields_patch = reqparse.RequestParser()
user_fields_patch.add_argument('nome', type=str, location='json')
user_fields_patch.add_argument('email', type=str, location='json')
user_fields_patch.add_argument('password', type=str, location='json')
