"""The main server application
"""
import logging
import os

import flask_cors
from flask import Flask

from server1 import oauth2
from server1.login import lm
from server1.models import db
from server1.special import handlers
from server1.views import bps


def create_app(test_config=None, **kwargs):
    app = Flask(__name__, instance_relative_config=True, **kwargs)

    # Default config
    app.config.from_mapping(
        SECRET_KEY="dev".encode(),
        SQLALCHEMY_DATABASE_URI="sqlite://",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SESSION_EXPIRES=60 * 60,
        USE_EXTRA_SERVER=True,
    )

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py")

    if not os.path.exists(app.instance_path):
        try:
            os.mkdir(app.instance_path)
        except OSError:
            print("Failed to create instance_path!")

    app.logger.setLevel(logging.DEBUG)
    app.logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Log to file
    fh = logging.FileHandler(os.path.join(app.instance_path, "server1.log"))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

    assert len(app.logger.handlers) == 1

    app.logger.info("Created new app instance")

    # Cross origin source sharing
    flask_cors.CORS(app)

    # Database
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    # Login manager
    lm.init_app(app)

    # OAuth2
    oauth2.config_oauth(app)

    # Blueprints
    for bp in bps:
        app.register_blueprint(bp)

    # Handlers
    for handler in handlers:
        app.register_error_handler(*handler)

    # Test route
    @app.route("/test")
    def test():
        return {"success": True}

    # Index
    app.add_url_rule("/", endpoint="index")

    return app
