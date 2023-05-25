from src.extensions.marshmallow import ma
from src.models.models import User


class UserReadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('id','password',)


class UserCreateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('id','password','uuid','created_at','updated_at',)

    name = ma.auto_field(required=True)
    cpf = ma.auto_field(required=True)
    email = ma.auto_field(required=True)
    phone_number = ma.auto_field(required=True)
    password = ma.auto_field(required=True)


class UserUpdateSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        exclude = ('id','password','uuid','created_at','updated_at',)
