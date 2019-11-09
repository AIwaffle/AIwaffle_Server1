import flask

import server1.api.model

bp = flask.Blueprint("api_model", __name__, url_prefix="/api/model")


@bp.route("/", methods=("POST",))
def root():
    x = flask.request.form.get("x", None)
    if not x:
        flask.abort(400)
    return server1.api.model.model(x)
