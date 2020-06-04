import hashlib
import os
import uuid
from typing import Union

import flask

from server1.models import db, User


def register(username: str, password: str) -> Union[str, bool]:
    flask.current_app.logger.debug("Registering new user {}".format(username))
    uf = User.query.filter(username == username).first()
    if uf is not None:
        flask.current_app.logger.error("User already registered")
        return False
    salt = os.urandom(4)
    salted = hashlib.sha512(password.encode() + salt).hexdigest()
    user = User(uuid.uuid4().hex, salt, username, salted)
    db.session.add(user)
    db.session.commit()
    flask.current_app.logger.debug("User registered")
    return user.uuid


def login(username: str, password: str) -> Union[User, None]:
    flask.current_app.logger.debug("Logging in {}".format(username))
    user = User.query.filter(username == username).first()

    if user is None:
        flask.current_app.logger.debug("User does not exist")
        return None

    salted = hashlib.sha512(password.encode() + user.salt).hexdigest()

    if salted == user.password:
        return user
    else:
        flask.current_app.logger.debug("No matching user record")
        return None
