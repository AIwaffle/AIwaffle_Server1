import flask
import flask_login
import pytest

from server1 import models


def test_register(client, app):
    response = client.post(
        "/api/auth/register", json={"username": "test_u2", "password": "a"},
    )
    assert response.json["success"]
    assert "uuid" in response.json

    with app.app_context():
        u = models.User.query.filter_by(username="test_u2").first()
        assert u is not None


@pytest.mark.parametrize(("username", "password", "message"), (
        ("", "", b"required",),
        ("a", "", b"required"),
        ("", "a", b"required"),
        ("test_u1", "a", b"User test_u1 already registered")
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/api/auth/register", json={"username": username, "password": password},
    )
    assert message in response.data


def test_login(client):
    response = client.post(
        "/api/auth/login", json={"username": "test_u1", "password": "a", "session": 1}
    )
    assert response.json["success"]

    with client:
        client.get("/")
        uuid = flask_login.current_user.get_id()
        user = models.User.query.filter_by(uuid=uuid).first()
        assert user.username == "test_u1"


@pytest.mark.parametrize(("username", "password", "message"), (
        ("a", "", b"required"),
        ("", "a", b"required"),
        ("a", "a", b"exist"),
        ("test_u1", "b", b"record"),
))
def test_login_validate_input(client, username, password, message):
    response = client.post(
        "/api/auth/login", json={"username": username, "password": password},
    )
    assert message in response.data


def test_current(client, auth):
    client.post(
        "/api/auth/login", json={"username": "test_u1", "password": "a", "session": 1}
    )
    response = client.get("/auth/current")
    assert response.json["username"] == "test_u1"


def test_logout(client, auth):
    client.post(
        "/api/auth/login", json={"username": "test_u1", "password": "a", "session": 1}
    )

    with client:
        auth.logout()
        assert "uuid" not in flask.session
