import hashlib
import json
import os
import time
import uuid

import server1.db
import server1.models


def register(username, password, db_session):
    uf = server1.models.User.query.filter(server1.models.User.username == username).first()
    print(server1.models.User.query.all())
    if uf is not None:
        return False
    salt = os.urandom(4)
    salted = hashlib.sha512(password.encode() + salt).hexdigest()
    user = server1.models.User(uuid.uuid4().hex, salt, username, salted)
    db_session.add(user)
    db_session.commit()
    return user.uuid


def login(username, password, db_session, session_expires):
    user = server1.models.User.query.filter(server1.models.User.username == username).first()

    if user is None:
        return False

    salted = hashlib.sha512(password.encode() + user.salt).hexdigest()

    expires = time.time() + session_expires
    expires = json.dumps(expires)
    if salted == user.password:
        token = hashlib.sha512(user.uuid.encode() + user.password.encode() + user.salt + expires.encode()).hexdigest()
        return {"uuid": user.uuid,
                "expires": expires,
                "token": token}
    else:
        return False


def load_logged_in_user(c_uuid, expires, token, db_session):
    user = server1.models.User.query.filter(server1.models.User.uuid == c_uuid).first()
    e_token = hashlib.sha512(user.uuid.encode() + user.password.encode() + user.salt + expires.encode()).hexdigest()
    if token == e_token:
        return user
    return None
