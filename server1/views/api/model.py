import uuid

import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("GET",))
def new():
    session_id = str(uuid.uuid4())
    server1.api.model.model("new", sid=session_id)
    return session_id


@bp.route("/iter", methods=("POST",))
def forward():
    session_id = flask.request.json.get("session_id", None)
    learning_rate = flask.request.json.get("learning_rate", 0.01)
    if session_id is None:
        flask.abort(400)
    return server1.api.model.model("iterate", sid=session_id, learning_rate=learning_rate)

