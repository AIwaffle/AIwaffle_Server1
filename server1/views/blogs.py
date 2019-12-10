import flask

bp = flask.Blueprint("blogs", __name__, url_prefix="/blogs")


@bp.route("/", methods=("GET",))
def root():
    pass
