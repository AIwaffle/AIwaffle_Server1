import json

import flask
import pytest

import server1.models


def test_forward(client, api_auth):
    response1 = api_auth.login()
    login_data = json.loads(response1.data)
    response2 = client.post(
        "/api/model/forward",
        data=login_data
    )
    assert response2.status_code == 200
    json.loads(response2.data)


def test_backward(client, api_auth):
    response1 = api_auth.login()
    login_data = json.loads(response1.data)
    response2 = client.post(
        "/api/model/backward",
        data=login_data
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 2


def test_loss(client, api_auth):
    response1 = api_auth.login()
    login_data = json.loads(response1.data)
    response2 = client.post(
        "/api/model/loss",
        data=login_data
    )
    assert response2.status_code == 200


def test_evaluate(client, api_auth):
    response1 = api_auth.login()
    login_data = json.loads(response1.data)
    response2 = client.post(
        "/api/model/evaluate",
        data=login_data
    )
    assert response2.status_code == 200


def test_model(client, api_auth):
    response1 = api_auth.login()
    login_data = json.loads(response1.data)
    response2 = client.post(
        "/api/model/model",
        data=login_data
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 7
