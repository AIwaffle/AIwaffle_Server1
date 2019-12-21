import json


def test_forward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]]}
    session_data = json.dumps(session_data)
    response2 = client.post(
        "/api/model/forward",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    json.loads(response2.data)


def test_backward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]], "Y": [1]}
    session_data = json.dumps(session_data)
    client.post(
        "/api/model/forward",
        data=session_data,
        content_type='application/json'
    )
    response2 = client.post(
        "/api/model/backward",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 2


def test_optimize(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]], "Y": [1]}
    session_data = json.dumps(session_data)
    client.post(
        "/api/model/forward",
        data=session_data,
        content_type='application/json'
    )
    client.post(
        "/api/model/backward",
        data=session_data,
        content_type='application/json'
    )
    response2 = client.post(
        "/api/model/optimize",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 2


def test_loss(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]], "Y": [1]}
    session_data = json.dumps(session_data)
    client.post(
        "/api/model/forward",
        data=session_data,
        content_type='application/json'
    )
    client.post(
        "/api/model/backward",
        data=session_data,
        content_type='application/json'
    )
    response2 = client.post(
        "/api/model/loss",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200


def test_model(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]], "Y": [1]}
    session_data = json.dumps(session_data)
    client.post(
        "/api/model/forward",
        data=session_data,
        content_type='application/json'
    )
    client.post(
        "/api/model/backward",
        data=session_data,
        content_type='application/json'
    )
    client.post(
        "/api/model/optimize",
        data=session_data,
        content_type='application/json'
    )
    response2 = client.post(
        "/api/model/model",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 2


def test_iter(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode(), "X": [[1.0, 2.0]], "Y": [1]}
    session_data = json.dumps(session_data)
    response2 = client.post(
        "/api/model/iter",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    assert len(json.loads(response2.data)) == 3
