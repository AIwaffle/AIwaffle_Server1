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
    session_id = flask.request.form.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("forward", sid=session_id)


@bp.route("/backward", methods=("POST",))
def backward():
    session_id = flask.request.form.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("backward", sid=session_id)


@bp.route("/evaluate", methods=("POST",))
def evaluate():
    session_id = flask.request.form.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("evaluate", sid=session_id)


@bp.route("/loss", methods=("POST",))
def loss():
    session_id = flask.request.form.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("loss", sid=session_id)


@bp.route("/model", methods=("POST",))
def model():
    session_id = flask.request.form.get("session_id", None)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("data", sid=session_id)
