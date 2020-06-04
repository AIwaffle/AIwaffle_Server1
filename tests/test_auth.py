import flask
import pytest

import server1.models


def test_register(client, app):
    assert client.get("/auth/register").status_code == 200
    response = client.post(
        "/auth/register", data={"username": "test_u2", "password": "a"},
    )
    assert response.headers["Location"] == "http://localhost/auth/login"

    with app.app_context():
        server1.db.get_db()
        u = server1.models.User.query.filter(server1.models.User.username == "test_u2").first()
        assert u is not None


@pytest.mark.parametrize(("username", "password", "message"), (
        ("", "", b"Field username and password is required.",),
        ("a", "", b"Field username and password is required."),
        ("", "a", b"Field username and password is required."),
        ("test_u1", "a", b"User test_u1 is already registered")
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password},
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "http://localhost/"

    with client:
        client.get("/")
        assert flask.g.user.username == "test_u1"


@pytest.mark.parametrize(("username", "password", "message"), (
        ("a", "", b"Field username and password is required."),
        ("", "a", b"Field username and password is required."),
        ("a", "a", b"Invalid username or password."),
        ("test_u1", "b", b"Invalid username or password."),
))
def test_login_validate_input(client, username, password, message):
    response = client.post(
        "/auth/login", data={"username": username, "password": password},
    )
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "uuid" not in flask.session
