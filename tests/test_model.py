import json

import flask
import pytest

import server1.models

def test_forward(client):
    response = client.get("/api/model/forward")
    assert response.status_code == 200
    json.loads(response.data)


def test_backward(client):
    response = client.get("/api/model/backward")
    assert response.status_code == 200
    json.loads(response.data)

def test_loss(client):
    response = client.get("/api/model/loss")
    assert response.status_code == 200

def test_evaluate(client):
    response = client.get("/api/model/evaluate")
    assert response.status_code == 200

def test_model(client):
    response = client.get("/api/model/model")
    assert response.status_code == 200
    assert len(json.loads(response.data)) == 7

