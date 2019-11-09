import os

import flask


def create_app(test_config=None):
    app = flask.Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite://",
        SESSION_EXPIRES=60 * 60,
    )

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import server1.db
    server1.db.init_app(app)

    import server1.views
    for bp in server1.views.bps:
        app.register_blueprint(bp)

    app.add_url_rule("/", endpoint="index")

    @app.route("/test")
    def test():
        return {"success": True}

    return app
