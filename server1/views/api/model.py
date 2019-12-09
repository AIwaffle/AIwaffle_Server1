import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/forward", methods=("GET",))
def forward():
    return server1.api.model.model("forward")


@bp.route("/backward", methods=("GET",))
def backward():
    return server1.api.model.model("backward")


@bp.route("/evaluate", methods=("GET",))
def evaluate():
    return server1.api.model.model("evaluate")


@bp.route("/loss", methods=("GET",))
def loss():
    return server1.api.model.model("loss")


@bp.route("/model", methods=("GET",))
def model():
    return server1.api.model.model("data")
