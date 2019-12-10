import flask

import server1.api.model
from .auth import login_required

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/forward", methods=("POST",))
@login_required
def forward():
    return server1.api.model.model("forward")


@bp.route("/backward", methods=("POST",))
@login_required
def backward():
    return server1.api.model.model("backward")


@bp.route("/evaluate", methods=("POST",))
@login_required
def evaluate():
    return server1.api.model.model("evaluate")


@bp.route("/loss", methods=("POST",))
@login_required
def loss():
    return server1.api.model.model("loss")


@bp.route("/model", methods=("POST",))
@login_required
def model():
    return server1.api.model.model("data")
