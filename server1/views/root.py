import flask

bp = flask.Blueprint("root", __name__)


@bp.route("/")
def index():
    return flask.render_template("index.html")
