import os
from dotenv import load_dotenv
from importlib import import_module
from dynaconf import FlaskDynaconf


def init_app(app):
    FlaskDynaconf(app)


def load_extensions(app):
    for extension in app.config.EXTENSIONS:
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)