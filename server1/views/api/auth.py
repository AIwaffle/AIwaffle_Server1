"""This module provides views with url prefix /api/auth
"""
import flask

import server1.api.auth
import server1.models

bp = flask.Blueprint("api_auth", __name__, url_prefix="/api/auth")


@bp.route("/register", methods=("POST",))
def register():
    """Register a new user

    POST /api/auth/register

    POST json data:
        username(str): the username of the new user
        password(str): the password of the new user

    Returns: a str, the uuid of the user

    Raises: flask.abort(400) when username or password is not provided or
    Raises: flask.abort(409) when user already exists
    """
    username = flask.request.json.get("username", None)
    password = flask.request.json.get("password", None)
    if not all((username, password)):
        flask.abort(400)
    db = server1.db.get_db()
    c_uuid = server1.api.auth.register(username, password)
    if c_uuid:
        return c_uuid
    else:
        flask.abort(409, "User already exists")


@bp.route("/login", methods=("POST",))
def login():
    """Login an existing user

    POST /api/auth/login

    POST json data:
        username(str): the username of the user
        password(str): the password of the user

    Returns: a json object
        uuid(str): the uuid of the user
        expires(float): the expire date of the user
        token(str): the login token
        All of these three are necessary for api login and verification

    Raises: flask.abort(400) when username or password is not provided or
        when the (username, password) is invalid
    """
    username = flask.request.json.get("username", None)
    password = flask.request.json.get("password", None)

    if not username or not password:
        flask.abort(400)
    db = server1.db.get_db()
    res = server1.api.auth.login(username, password,
                                 flask.current_app.config["SESSION_EXPIRES"])
    if not res:
        flask.abort(400)
    else:
        return res
