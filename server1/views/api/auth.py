"""/api/auth

Not implemented
"""
from flask import (
    abort,
    Blueprint,
)


bp = Blueprint("api_auth", __name__, url_prefix="/api/auth")


@bp.route("/register", methods=("POST",))
def register():
    """Register a new user

    POST /api/auth/register

    POST json data:
        username(str): the username
        password(str): the password

    Returns: (str) the uuid of the user

    Raises: flask.abort(400) when username or password is not provided or
    Raises: flask.abort(409) when user already exists
    """
    abort(501)


@bp.route("/login", methods=("POST",))
def login():
    """Login an existing user

    POST /api/auth/login

    POST json data:
        username(str): the username
        password(str): the password

    Returns: a json object
        uuid(str): the uuid of the user
        expires(float): the expire date of the user
        token(str): the login token
        All of these three are necessary for api login and verification

    Raises: flask.abort(400) when username or password is not provided or
        when the (username, password) is invalid
    """
    abort(501)
