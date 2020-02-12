"""This module provides views with url prefix /api/model
"""
import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("POST",))
def new():
    """Create a new instance

    POST /api/model/new

    Returns: a str, the session id
    """
    res = server1.api.model.model("new")
    return res["session_id"]


@bp.route("/iter", methods=("POST",))
def iter_():
    """Iterate the model

    POST /api/model/iter

    TODO: Complete docs for model
    """
    if flask.request.json is None:
        session_id = flask.request.form.get("session_id", None)
        epoch_num = flask.request.form.get("epoch_num", 1)
        learning_rate = flask.request.form.get("learning_rate", 0.01)
    else:
        session_id = flask.request.json.get("session_id", None)
        epoch_num = flask.request.json.get("epoch_num", 1)
        learning_rate = flask.request.json.get("learning_rate", 0.01)
    if session_id is None:
        flask.abort(400)
    res = server1.api.model.model("iterate", session_id=session_id, learning_rate=learning_rate, epoch_num=epoch_num)
    if res["code"] != 200:
        flask.abort(res["code"])
    if not isinstance(res, dict):
        flask.abort(400)
    res.__delitem__("code")
    return res
