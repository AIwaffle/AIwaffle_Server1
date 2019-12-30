import json


def test_forward(client, api_model):
    response1 = api_model.new()
    session_data = {"session_id": response1.data.decode()}
    session_data = json.dumps(session_data)
    response2 = client.post(
        "/api/model/iter",
        data=session_data,
        content_type='application/json'
    )
    assert response2.status_code == 200
    resp = json.loads(response2.data)
    assert len(resp) == 6
