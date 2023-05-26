import os

# CRIPT
ALGORITHM = 'HS512'

# EXTENSIONS
EXTENSIONS = [
    'src.extensions.database:init_app',
    'src.extensions.cache:init_app',
    'src.extensions.csrf:init_app',
    'src.extensions.swagger:init_app',
    'src.extensions.marshmallow:init_app',
]

# RESOURCES
RESOURCES = [
    'src.api.v1.users:init_app',
]


# KEYS
SECRET_KEY = os.environ.get('SECRET_KEY')

# REDIS - CACHE
CACHE_TYPE = os.environ.get('CACHE_TYPE')
CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST')
CACHE_REDIS_PORT = os.environ.get('CACHE_REDIS_PORT')
CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB')
CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL')
CACHE_DEFAULT_TIMEOUT= os.environ.get('CACHE_DEFAULT_TIMEOUT')

# DB
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
