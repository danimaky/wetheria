from flask import Flask

from wetheria.extensions import (
    cache,
    api
)


def create_app(config_object="wetheria.settings"):
    """
    Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

        Args:
            config_object: (str) The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """
    Register Flask extensions.

    Args:
        app: Flask application

    """
    cache.init_app(app)
    api.init_app(app)
    return


app = create_app()
