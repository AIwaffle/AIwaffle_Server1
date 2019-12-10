import functools

import flask

import server1.api.auth
import server1.db
import server1.models

bp = flask.Blueprint("api_auth", __name__, url_prefix="/api/auth")


@bp.route("/register", methods=("POST",))
def register():
    username = flask.request.form.get("username", None)
    password = flask.request.form.get("password", None)

    if not username or not password:
        flask.abort(400)

    db = server1.db.get_db()

    c_uuid = server1.api.auth.register(username, password, db)

    if c_uuid:
        return {"success": True, "uuid": c_uuid}
    else:
        error = "User {} is already registered.".format(username)
        return {"success": False, "reason": error}, 400


@bp.route("/login", methods=("POST",))
def login():
    username = flask.request.form.get("username", None)
    password = flask.request.form.get("password", None)

    if not username or not password:
        flask.abort(400)

    db = server1.db.get_db()

    res = server1.api.auth.login(username, password, db,
                                 flask.current_app.config["SESSION_EXPIRES"])
    if not res:
        flask.abort(400)
    else:
        return res


@bp.before_app_request
def load_logged_in_user():
    db = server1.db.get_db()
    c_uuid = flask.request.form.get("uuid", None)
    expires = flask.request.form.get("expires", None)
    token = flask.session.form.get("token", None)
    if c_uuid is None or expires is None or token is None:
        flask.g.user = None
        return
    else:
        flask.g.user = server1.api.auth.load_logged_in_user(c_uuid, expires, token, db)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if flask.g.user is None:
            flask.abort(400)

        return view(**kwargs)

    return wrapped_view
