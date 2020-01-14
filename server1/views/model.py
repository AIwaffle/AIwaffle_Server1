"""This module provides views with url prefix /model
"""
import flask

bp = flask.Blueprint("model", __name__, url_prefix="/model")


@bp.route("/", methods=("GET",))
def root():
    """The model page

    GET /model

    Returns: the model page
    """
    return flask.render_template("model.html")
