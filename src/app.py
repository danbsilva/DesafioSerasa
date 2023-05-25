from flask import Flask, redirect, url_for
from src.extensions import configuration


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)

    @app.get('/')
    def index():
        return redirect(url_for('index'))

    return app



