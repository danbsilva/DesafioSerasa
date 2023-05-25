from flask_script import Manager


def init_app(app):
    Manager(app)
    app = app

    