from functools import wraps
from flask import request, current_app


from typing import Any, Union
from datetime import datetime, timedelta
from jose import jwt

from src.models.models import User


def create_token_jwt(subject: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(days=int(1))
    to_encode = {"exp": expire, "uuid": str(subject)}
    encoded_jwt = jwt.encode(to_encode, current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])
    return encoded_jwt


def verify_token(f):
    """
    Decorator to check if the user is authenticated
    token: the token to be checked user is authenticated or not from header
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        access_token = None

        try:
            access_token = request.headers['Authorization']
        except: ...

        if not access_token:
            return {'message': 'Access-Token não encontrado'}, 401

        try:
            carga = jwt.decode(access_token, current_app.config['SECRET_KEY'], algorithms=[current_app.config['ALGORITHM']])
            current_user = User.query.filter_by(uuid=carga['uuid']).first()
        except:
            return {'message': 'Access-Token inválido'}, 401

        return f(*args, **kwargs)

    return decorated
