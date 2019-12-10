import json

import flask
import pytest

import server1.models


def test_forward(client):
    response = client.post(
        "/api/model/forward",
        data={"username": "test_u1", "password": "a"}
    )
    assert response.status_code == 200
    json.loads(response.data)


def test_backward(client):
    response = client.post(
        "/api/model/backward",
        data={"username": "test_u1", "password": "a"}
    )
    assert response.status_code == 200
    assert len(json.loads(response.data)) == 2


def test_loss(client):
    response = client.post(
        "/api/model/loss",
        data={"username": "test_u1", "password": "a"}
    )
    assert response.status_code == 200


def test_evaluate(client):
    response = client.post(
        "/api/model/evaluate",
        data={"username": "test_u1", "password": "a"}
    )
    assert response.status_code == 200


def test_model(client):
    response = client.post(
        "/api/model/model",
        data={"username": "test_u1", "password": "a"}
    )
    assert response.status_code == 200
    assert len(json.loads(response.data)) == 7
