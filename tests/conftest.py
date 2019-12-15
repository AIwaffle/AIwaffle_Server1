import os
import tempfile

import pytest

import server1
import server1.db
import server1.models


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = server1.create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_path,
        }
    )

    with app.app_context():
        server1.db.init_db()
        server1.db.get_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    res = app.test_client()
    res.post("/auth/register", data={"username": "test_u1", "password": "a"})
    return res


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="test_u1", password="a"):
        return self._client.post("/auth/login", data={"username": username, "password": password})

    def logout(self):
        return self._client.get("/auth/logout")


class APIModelActions:
    def __init__(self, client):
        self._client = client

    def new(self):
        return self._client.get("/api/model/new")


@pytest.fixture
def auth(client):
    return AuthActions(client)


@pytest.fixture
def api_model(client):
    return APIModelActions(client)
