import sqlalchemy

from server1.db import Base


class User(Base):
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
