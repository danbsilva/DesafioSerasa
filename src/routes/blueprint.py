from flask import Blueprint
from src.controllers.index_constroller import index

bp = Blueprint('blueprint', __name__)

bp.route('/', methods=['GET'])(index)


def init_app(app):
    app.register_blueprint(bp, url_prefix='/machines')