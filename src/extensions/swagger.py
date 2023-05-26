from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

docs = FlaskApiSpec()


def init_app(app):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='DesafioSerasa',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        )
    })
    docs.init_app(app)
