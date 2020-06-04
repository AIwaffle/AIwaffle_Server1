import time

import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):
    """The user database object
    """
    __tablename__ = "users"

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

    def check_password(self, password):
        return password == self.password

    def __repr__(self):
        return "<User {}>".format(self.username)
