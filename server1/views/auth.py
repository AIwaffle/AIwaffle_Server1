"""/auth
"""
import flask_login
from flask import (
    request, flash, redirect, url_for, render_template, jsonify,
    Blueprint,
)

from server1.api import auth

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user

    GET /auth/register

        Returns:
            The register page

    POST /auth/register

        POST form data:
            username(str): the username
            password(str): the password

        Returns:
            flask.redirect(auth.login) if the register is success
            The register page with error message if the register fails
    """
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            user = auth.register(username, password)
            if user:
                return redirect(url_for("auth.login"))
            else:
                error = "User {} is already registered.".format(username)

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Login the user

    GET /auth/login

        Returns:
            The login page

    POST /auth/login

        POST form data:
            username(str): the username
            password(str): the password

        Returns:
            flask.redirect(index) if success
                also sets cookie for the login manager
            The login page with error if fails
    """
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        error = None

        if not username or not password:
            error = "Field username and password is required."

        if error is None:
            user = auth.login(username, password)
            if not user:
                error = "Invalid username or password."
            else:
                flask_login.login_user(user)
                # next = flask.request.args.get('next')
                return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
@flask_login.login_required
def logout():
    """Logout the user

    /auth/logout

    Returns:
        flask.redirect(index)
    """
    flask_login.logout_user()
    return redirect(url_for("index"))


@bp.route("/current", methods=("GET",))
@flask_login.login_required
def current():
    """Get current user

    GET /auth/current

        Returns:
            dict{uuid, username}
    """

    c_uuid = flask_login.current_user.get_id()
    user = auth.get_user(uuid=c_uuid)
    return jsonify(uuid=c_uuid, username=user.username)
