import json


def test_forward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode()}
    response2 = client.post(
        "/api/model/iter",
        data=dict(session_id=response1.data.decode())
    )
    assert response2.status_code == 200
    resp = json.loads(response2.data)
    assert len(resp) == 7
    assert 'accuracy' in resp
    assert 'loss' in resp
    assert 'X' in resp
    assert 'Y' in resp
    assert 'avg_loss' in resp
    assert 'W' in resp
    assert 'dW' in resp
