from src.extensions.database import db
from flask_serialize import FlaskSerialize

fs_mixin = FlaskSerialize(db)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    uuid = db.Column(db.String, index=True)
    name = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

    def __repr__(self):
        return '{}'.format(self.nome)

