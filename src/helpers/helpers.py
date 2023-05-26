from functools import wraps
from flask_restful import output_json
from src.api.security.cryptography import encrypt


def verify_record_exists(model, key, crypt=False):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            cls = model
            k = list(kwargs.keys())[list(kwargs.values()).index(kwargs[key])]
            if crypt:
                value = {k: encrypt(kwargs[key])}
            else:
                value = {k: kwargs[key]}
            obj = cls.query.filter_by(**value).first()
            if obj: return output_json({'message': f'{cls.__name__} already exists'}, 400)
            return func(*args, **kwargs)
        return decorated
    return wrapper