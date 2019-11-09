import functools

import flask

import server1.api.auth
import server1.db
import server1.models

bp = flask.Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if flask.request.method == "POST":
        username = flask.request.form.get("username", None)
        password = flask.request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            db = server1.db.get_db()
            c_uuid = server1.api.auth.register(username, password, db)
            if c_uuid:
                return flask.redirect(flask.url_for("auth.login"))
            else:
                error = "User {} is already registered.".format(username)

        flask.flash(error)

    return flask.render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get("username", None)
        password = flask.request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            db = server1.db.get_db()
            res = server1.api.auth.login(username, password, db,
                                         flask.current_app.config["SESSION_EXPIRES"])
            if not res:
                error = "Invalid username or password."
            else:
                flask.session.clear()
                flask.session["uuid"] = res["uuid"]
                flask.session["expires"] = res["expires"]
                flask.session["token"] = res["token"]
                return flask.redirect(flask.url_for("index"))

        flask.flash(error)

    return flask.render_template("auth/login.html")


@bp.route("/logout", methods=("GET", "POST"))
def logout():
    flask.session.clear()
    return flask.redirect(flask.url_for("index"))


@bp.before_app_request
def load_logged_in_user():
    db = server1.db.get_db()
    c_uuid = flask.session.get("uuid", None)
    expires = flask.session.get("expires", None)
    token = flask.session.get("token", None)
    if c_uuid is None or expires is None or token is None:
        flask.g.user = None
        return
    else:
        flask.g.user = server1.api.auth.load_logged_in_user(c_uuid, expires, token, db)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if flask.g.user is None:
            return flask.redirect(flask.url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
