import os
import uuid
from typing import Union

from flask import current_app

from server1.models import db, User


def get_user(**kwargs) -> Union[User, None]:
    """Alias for first user returned by User.query.filter_by
    """
    return User.query.filter_by(**kwargs).first()


def register(username: str, password: str) -> Union[User, None]:
    """Register a user by username and password

    Returns:
        The user when success
        None when not success
    """
    user = get_user(username=username)
    if user is not None:
        current_app.logger.debug("User {} already registered".format(username))
        return None

    salt = os.urandom(4)
    salted = User.salt_password(password, salt)
    user = User(uuid.uuid4().hex, salt, username, salted)

    db.session.add(user)
    db.session.commit()

    current_app.logger.info("User {} registered".format(username))
    return user


def login(username: str, password: str) -> Union[User, None, bool]:
    """Login a user by username and password

    Returns:
        The user when success
        None when user does not exists
        False when password does not match
    """
    user = get_user(username=username)

    if user is None:
        current_app.logger.debug("User {} does not exist".format(username))
        return None

    if user.check_password(password):
        current_app.logger.debug("User {} logged in".format(username))
        return user

    current_app.logger.debug("No matching record for user {}".format(username))
    return False
