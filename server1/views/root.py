"""/
"""
from flask import (
    render_template, abort, Blueprint,
)

bp = Blueprint("root", __name__)


@bp.route("/")
def index():
    """The index page

    GET /

    Returns: the index page
    """
    return render_template("index.html")
    # return flask.send_from_directory("../AIWaffle-website/dist", "index.html")


@bp.route("/teapot")
def teapot():
    """Easter egg

    Raises: flask.abort(418)
    """
    abort(418)
