from flask import Flask, redirect, url_for
from src.config import load_settings

# Load Environments
from dotenv import load_dotenv
load_dotenv()


def minimal_app(**configs):
    app = Flask(__name__)
    load_settings.init_app(app, **configs)
    return app


def create_app(**configs):
    app = minimal_app(**configs)

    @app.get('/')
    def index():
        return redirect(url_for('index'))

    return app


