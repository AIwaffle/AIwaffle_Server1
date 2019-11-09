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
