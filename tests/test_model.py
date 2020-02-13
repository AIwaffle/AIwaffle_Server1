import json


def test_forward(client):
    for i in range(5):
        response1 = client.post(
            "/api/model/new"
        )
        response2 = client.post(
            "/api/model/iter",
            data=dict(session_id=response1.data.decode(),
                      epoch_num=150)
        )
        assert response2.status_code == 200
        resp = json.loads(response2.data)
        assert len(resp) == 8
        assert 'A' in resp
        assert 'accuracy' in resp
        assert 'loss' in resp
        assert 'X' in resp
        assert 'Y' in resp
        assert 'avg_loss' in resp
        assert 'W' in resp
        assert 'dW' in resp
