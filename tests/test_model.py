import json

import flask
import pytest

import server1.models


def test_forward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data}
    response2 = client.post(
        "/api/model/forward",
        data=session_data
    )
    assert response2.status_code == 200
    json.loads(response2.data)


def test_backward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data}
    client.post(
        "/api/model/forward",
        data=session_data
    )
    response2 = client.post(
        "/api/model/backward",
        data=session_data
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 2


def test_loss(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data}
    response2 = client.post(
        "/api/model/loss",
        data=session_data
    )
    assert response2.status_code == 200


def test_evaluate(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data}
    response2 = client.post(
        "/api/model/evaluate",
        data=session_data
    )
    assert response2.status_code == 200


def test_model(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data}
    response2 = client.post(
        "/api/model/model",
        data=session_data
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 7
