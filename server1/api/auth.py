import hashlib
import json
import os
import time
import uuid

import flask

import server1.db
import server1.models


def register(username, password, db_session):
    flask.current_app.logger.debug("Registering new user {}".format(username))
    uf = server1.models.User.query.filter(server1.models.User.username == username).first()
    if uf is not None:
        flask.current_app.logger.error("User already registered")
        return False
    salt = os.urandom(4)
    salted = hashlib.sha512(password.encode() + salt).hexdigest()
    user = server1.models.User(uuid.uuid4().hex, salt, username, salted)
    db_session.add(user)
    db_session.commit()
    flask.current_app.logger.debug("User registered")
    return user.uuid


def login(username, password, db_session, session_expires):
    """

    Args:
        username ():
        password ():
        db_session ():
        session_expires ():

    Returns:

    """
    flask.current_app.logger.debug("Logging in {}".format(username))
    user = server1.models.User.query.filter(server1.models.User.username == username).first()

    if user is None:
        flask.current_app.logger.debug("User does not exist")
        return False

    salted = hashlib.sha512(password.encode() + user.salt).hexdigest()

    expires = time.time() + session_expires
    expires = json.dumps(expires)
    if salted == user.password:
        token = hashlib.sha512(user.uuid.encode() + user.password.encode() + user.salt + expires.encode()).hexdigest()
        flask.current_app.logger.debug("Login success")
        return {"uuid": user.uuid,
                "expires": expires,
                "token": token}
    else:
        flask.current_app.logger.debug("No matching user record")
        return False


def load_logged_in_user(c_uuid, expires, token, db_session):
    user = server1.models.User.query.filter(server1.models.User.uuid == c_uuid).first()
    e_token = hashlib.sha512(user.uuid.encode() + user.password.encode() + user.salt + expires.encode()).hexdigest()
    # TODO: `Expires` not used
    if token == e_token:
        return user
    return None
