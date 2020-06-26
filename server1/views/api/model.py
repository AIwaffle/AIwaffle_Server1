"""/api/model
"""
from flask import (
    request, abort, jsonify,
    Blueprint,
)

from server1.api.model import model

bp = Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("POST",))
def new():
    """Create a new instance

    POST /api/model/new

    Returns: a str, the session id
    """
    res = model("new")
    return res["session_id"]


@bp.route("/iter", methods=("POST",))
def iter_():
    """Iterate the model

    POST /api/model/iter

    TODO: Complete docs for model
    """
    if request.json is None:
        session_id = request.form.get("session_id", None)
        epoch_num = request.form.get("epoch_num", 1)
        learning_rate = request.form.get("learning_rate", 0.01)
    else:
        session_id = request.json.get("session_id", None)
        epoch_num = request.json.get("epoch_num", 1)
        learning_rate = request.json.get("learning_rate", 0.01)
    if session_id is None:
        abort(400)
    res = model("iterate", session_id=session_id, learning_rate=learning_rate, epoch_num=epoch_num)
    if res["code"] != 200:
        abort(res["code"])
    if not isinstance(res, dict):
        abort(400)
    res.__delitem__("code")
    return jsonify(res)
