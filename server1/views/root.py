"""This module provides view with url prefix /
"""
import flask

bp = flask.Blueprint("root", __name__)


@bp.route("/")
def index():
    """The index page

    GET /

    Returns: the index page
    """
    # return flask.render_template("index.html")
    return flask.send_from_directory("../AIWaffle-website/dist", "index.html")


@bp.route("/dist/<path:path>")
def dist(path):
    return flask.send_from_directory("../AIWaffle-website/dist", path)


@bp.route("/assets/<path:path>")
def assets(path):
    return flask.send_from_directory("../AIWaffle-website/assets", path)


@bp.route("/teapot")
def teapot():
    """Easter egg

    Raises: flask.abort(418)
    """
    flask.abort(418)
