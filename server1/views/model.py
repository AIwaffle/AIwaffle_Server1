import flask

bp = flask.Blueprint("model", __name__, url_prefix="/model")


@bp.route("/", methods=("GET",))
def root():
    return flask.render_template("model.html")
