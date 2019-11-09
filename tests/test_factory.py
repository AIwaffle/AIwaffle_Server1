import json

import server1


def test_config():
    assert not server1.create_app().testing
    assert server1.create_app({"TESTING": True}).testing


def test_test(client):
    response = client.get("/test")
    assert json.loads(response.data).get("success", False) == True
