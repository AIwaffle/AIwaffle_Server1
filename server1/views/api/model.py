import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/new", methods=("GET",))
def new():
    pass


@bp.route("/forward", methods=("POST",))
def forward():
    return server1.api.model.model("forward")


@bp.route("/backward", methods=("POST",))
def backward():
    return server1.api.model.model("backward")


@bp.route("/evaluate", methods=("POST",))
def evaluate():
    return server1.api.model.model("evaluate")


@bp.route("/loss", methods=("POST",))
def loss():
    return server1.api.model.model("loss")


@bp.route("/model", methods=("POST",))
def model():
    return server1.api.model.model("data")
