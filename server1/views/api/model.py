import uuid

import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("GET",))
def new():
    session_id = str(uuid.uuid4())
    server1.api.model.model("new", sid=session_id)
    return session_id


@bp.route("/forward", methods=("POST",))
def forward():
    session_id = flask.request.json.get("session_id", None)
    x = flask.request.json.get("X", None)
    if session_id is None or x is None:
        flask.abort(400)
    return server1.api.model.model("forward", sid=session_id, X=x)


@bp.route("/backward", methods=("POST",))
def backward():
    session_id = flask.request.json.get("session_id", None)
    y = flask.request.json.get("Y", None)
    if session_id is None or y is None:
        flask.abort(400)
    return server1.api.model.model("backward", sid=session_id, Y=y)


@bp.route("/optimize", methods=("POST",))
def optimize():
    session_id = flask.request.json.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("optimize", sid=session_id)


@bp.route("/loss", methods=("POST",))
def loss():
    session_id = flask.request.json.get("session_id", None)
    y = flask.request.json.get("Y", None)
    if session_id is None or y is None:
        flask.abort(400)
    return server1.api.model.model("loss", sid=session_id, Y=y)


@bp.route("/model", methods=("POST",))
def model():
    session_id = flask.request.json.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("data", sid=session_id)


@bp.route("/iter", methods=("POST",))
def iter_():
    session_id = flask.request.json.get("session_id", None)
    x = flask.request.json.get("X", None)
    y = flask.request.json.get("Y", None)
    if session_id is None or x is None or y is None:
        flask.abort(400)
    return server1.api.model.model("iter", sid=session_id, X=x, Y=y)
