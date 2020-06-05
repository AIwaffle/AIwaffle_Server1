"""This module provides views with url prefix /auth
"""
import flask
import flask_login

from server1.api import auth

bp = flask.Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user

    GET /auth/register

    Returns: the register page

    POST /auth/register

    POST form data:
        username(str): the username of the new user
        password(str): the password of the new user

    Returns:
        flask.redirect(auth.login) if the register is success
        the register page with error message if the register fails
    """
    if flask.request.method == "POST":
        username = flask.request.form.get("username", None)
        password = flask.request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            c_uuid = auth.register(username, password)
            if c_uuid:
                return flask.redirect(flask.url_for("auth.login"))
            else:
                error = "User {} is already registered.".format(username)

        flask.flash(error)

    return flask.render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Login the user

    GET /auth/login

    Returns: the login page

    POST /auth/login

    POST form data:
        username(str): the username
        password(str): the password

    Returns:
        flask.redirect(index) if success
            also sets cookie for the user
            that is necessary for load_logged_in_user
        login web page with error if fails
    """
    if flask.request.method == "POST":
        username = flask.request.form.get("username", None)
        password = flask.request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            user = auth.login(
                username, password,
            )
            if not user:
                error = "Invalid username or password."
            else:
                flask_login.login_user(user)
                # next = flask.request.args.get('next')
                return flask.redirect(flask.url_for("index"))

        flask.flash(error)

    return flask.render_template("auth/login.html")


@bp.route("/logout")
@flask_login.login_required
def logout():
    """Logout the user

    /auth/logout

    Returns: flask.redirect(index)
    """
    flask_login.logout_user()
    return flask.redirect(flask.url_for("index"))


@bp.route("/current")
@flask_login.login_required
def current():
    """Get current user

    /auth/current

    Returns: the id of the user
    """
    return flask_login.current_user.get_id()
