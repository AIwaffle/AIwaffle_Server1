import datetime

import sqlalchemy

from server1.db import Base


class User(Base):
    """The user database object

    Should NEVER be passed outside the backend!
    """
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    uuid = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    salt = sqlalchemy.Column(sqlalchemy.Binary, nullable=False)

    username = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __init__(self, uuid, salt, username, password):
        self.uuid = uuid
        self.salt = salt
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User uuid={}, username={}>".format(self.uuid, self.username)


class Post(Base):
    __tablename__ = "posts"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    author_uuid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.uuid"), nullable=False)
    created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.datetime.utcnow)

    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    body = sqlalchemy.Column(sqlalchemy.String)

    def __init__(self, author_uuid, created, title, body):
        self.author_uuid = author_uuid
        self.created = created
        self.title = title
        self.body = body


class Statistics(Base):
    __tablename__ = "statistics"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    access_total = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __init__(self, id_):
        self.id = id_

