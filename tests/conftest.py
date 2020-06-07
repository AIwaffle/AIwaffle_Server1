import os
import tempfile

import pytest

import server1


@pytest.fixture
def app():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.mkdir(os.path.join(temp_dir, "instance"))
        app = server1.create_app(
            test_config={
                "TESTING": True,
                "SQLALCHEMY_DATABASE_URI": "sqlite:///{}".format(
                    os.path.join(temp_dir, "server1.db")
                ),
                "USE_EXTRA_SERVER": False,
            },
            instance_path=os.path.join(temp_dir, "instance")
        )
        yield app


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
        return self._client.post("/api/model/new")


@pytest.fixture
def auth(client):
    return AuthActions(client)


@pytest.fixture
def api_model(client):
    return APIModelActions(client)
