import logging
import os

import flask
import flask.logging
import flask_cors


def create_app(test_config=None):
    app = flask.Flask(__name__, instance_relative_config=True)
    flask_cors.CORS(app)

    module_logger = logging.getLogger(__name__)

    assert module_logger is app.logger

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite://",
        SESSION_EXPIRES=60 * 60,
        USE_EXTRA_SERVER=True,
    )

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    assert isinstance(app.logger, logging.Logger)
    app.logger.setLevel(logging.DEBUG)
    app.logger.handlers.clear()
    fh = logging.FileHandler(os.path.join(os.curdir, "instance", "server1.log"))
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

    app.logger.info("Created new app instance")

    import server1.db
    server1.db.init_app(app)

    import server1.views
    for bp in server1.views.bps:
        app.register_blueprint(bp)

    app.add_url_rule("/", endpoint="index")

    @app.route("/test")
    def test():
        return {"success": True}

    @app.errorhandler(404)
    def handle404(e):
        return flask.send_from_directory("../AIWaffle-website/dist", "index.html"), 404

    return app
