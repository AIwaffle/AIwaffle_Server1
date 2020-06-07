import hashlib
import time

import flask_sqlalchemy
from authlib.integrations import sqla_oauth2

db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):
    """The user database object
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.String, unique=True, nullable=False)
    salt = db.Column(db.Binary, nullable=False)

    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, uuid, salt, username, password):
        self.uuid = uuid
        self.salt = salt
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return self.uuid

    def get_user_id(self):
        return self.uuid

    def check_password(self, password):
        salted = hashlib.sha512(password.encode() + self.salt).hexdigest()
        return salted == self.password

    def __repr__(self):
        return "<User {}>".format(self.username)


"""Sample implementation from
https://github.com/authlib/example-oauth2-server/blob/master/website/models.py
"""


class OAuth2Client(db.Model, sqla_oauth2.OAuth2ClientMixin):
    __tablename__ = "oauth2_client"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.uuid", ondelete="CASCADE"))
    user = db.relationship("User")


class OAuth2AuthorizationCode(db.Model, sqla_oauth2.OAuth2AuthorizationCodeMixin):
    __tablename__ = "oauth2_code"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.uuid", ondelete="CASCADE"))
    user = db.relationship("User")


class OAuth2Token(db.Model, sqla_oauth2.OAuth2TokenMixin):
    __tablename__ = "oauth2_token"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.uuid", ondelete="CASCADE"))
    user = db.relationship("User")

    def is_refresh_token_active(self):
        if self.revoked:
            return False
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at >= time.time()
