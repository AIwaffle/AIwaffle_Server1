import logging
import os

import flask
import flask.logging
import flask_cors

import server1.special
from server1 import special
from server1.login import lm
from server1.models import db
from server1.oauth2 import config_oauth
from server1.special import handlers
from server1.views import bps


def create_app(test_config=None, **kwargs):
    app = flask.Flask(__name__, instance_relative_config=True, **kwargs)

    module_logger = logging.getLogger(__name__)

    assert module_logger is app.logger

    app.config.from_mapping(
        SECRET_KEY="dev".encode(),
        SQLALCHEMY_DATABASE_URI="sqlite://",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SESSION_EXPIRES=60 * 60,
        USE_EXTRA_SERVER=False,
    )

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py")

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    assert isinstance(app.logger, logging.Logger)
    app.logger.setLevel(logging.DEBUG)
    app.logger.handlers.clear()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler(os.path.join(app.instance_path, "server1.log"))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # ch.setFormatter(formatter)
    # app.logger.addHandler(ch)

    assert len(app.logger.handlers) >= 1
    app.logger.info("Created new app instance")

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route("/test")
    def test():
        return {"success": True}

    for bp in bps:
        app.register_blueprint(bp)

    for handler in handlers:
        app.register_error_handler(*handler)

    app.add_url_rule("/", endpoint="index")

    flask_cors.CORS(app)
    db.init_app(app)
    lm.init_app(app)
    config_oauth(app)

    return app
