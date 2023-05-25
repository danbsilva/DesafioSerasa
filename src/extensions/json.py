from flask_json import FlaskJSON


def init_app(app):
    FlaskJSON(app)
    