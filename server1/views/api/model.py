import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/model", methods=("GET",))
def model():
    return server1.api.model.model("model")


@bp.route("/params", methods=("GET", "POST"))
def params():
    if flask.request.method == "POST":
        data = flask.request.get_json()
        learning_rate = data.get("learningRate", None)
        if learning_rate:
            return server1.api.model.model("params", learning_rate=learning_rate)
    return server1.api.model.model("params")


@bp.route("/forward", methods=("POST",))
def forward():
    data = flask.request.get_json()
    x = data.get("X", None)
    if not x:
        flask.abort(400)
    return server1.api.model.model("forward", X=x)


@bp.route("/backward", methods=("GET",))
def backward():
    return server1.api.model.model("backward")


@bp.route("/output", methods=("GET",))
def output():
    return server1.api.model.model("output")


@bp.route("/optimize", methods=("GET",))
def optimize():
    server1.api.model.model("optimize")
    return ""
