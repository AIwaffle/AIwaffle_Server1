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
    return flask.render_template("index.html")


@bp.route("/teapot")
def teapot():
    """Easter egg

    Raises: flask.abort(418)
    """
    flask.abort(418)
