"""/api/auth
"""
from typing import Tuple

import flask_login
from flask import (
    abort, request, jsonify,
    Blueprint)

from server1.api import auth

bp = Blueprint("api_auth", __name__, url_prefix="/api/auth")


def get_info() -> Tuple[str, str]:
    if request.json is not None:
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if all((username, password,)):
            return username, password

    abort(jsonify(
        success=False,
        reason="Field username and password is required",
    ))


@bp.route("/register", methods=("POST",))
def register():
    """Register a new user

    POST /api/auth/register

    POST json data:
        username(str): the username
        password(str): the password
    TODO
    """
    username, password = get_info()

    user = auth.register(username, password)

    if user is not None:
        return jsonify(
            success=True,
            uuid=user.uuid,
        )

    return jsonify(
        success=False,
        reason="User {} already registered".format(username),
    )


@bp.route("/login", methods=("POST",))
def login():
    """Login an existing user

    POST /api/auth/login

    POST json data:
        username(str): the username
        password(str): the password
        session(bool): whether to store cookies
    """
    username, password = get_info()

    user = auth.login(username, password)

    if user is None:
        return jsonify(
            success=False,
            reason="User {} does not exist".format(username),
        )
    elif not user:
        return jsonify(
            success=False,
            reason="No matching record for user {}".format(username),
        )

    if request.json.get("session", 0) == 1:
        flask_login.login_user(user)
        return jsonify(
            success=True,
        )

    abort(501)
