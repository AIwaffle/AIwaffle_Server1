"""This module provides view with url prefix /
"""
import os
import flask

bp = flask.Blueprint("root", __name__)


@bp.route("/")
def index():
    """The index page

    GET /

    Returns: the index page
    """
    print(os.curdir)
    return flask.render_template("index.html")
    # return flask.send_from_directory("../AIWaffle-website/dist", "index.html")


@bp.route("/teapot")
def teapot():
    """Easter egg

    Raises: flask.abort(418)
    """
    flask.abort(418)
