"""This module provides views with url prefix /api/model
"""
import uuid

import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("POST",))
def new():
    """Create a new instance

    POST /api/model/new

    Returns: a str, the session id
    """
    session_id = str(uuid.uuid4())
    server1.api.model.model("new", sid=session_id)
    return session_id


@bp.route("/iter", methods=("POST",))
def iter_():
    """Iterate the model

    POST /api/model/iter

    TODO: Complete docs for model
    """
    if flask.request.json is None:
        session_id = flask.request.form.get("session_id", None)
        learning_rate = flask.request.form.get("learning_rate", 0.01)
    else:
        session_id = flask.request.json.get("session_id", None)
        learning_rate = flask.request.json.get("learning_rate", 0.01)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("iterate", sid=session_id, learning_rate=learning_rate)
