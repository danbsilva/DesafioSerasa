from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_rest_paginate import Pagination


db = SQLAlchemy()
pagination = Pagination()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    pagination.init_app(app,db)
