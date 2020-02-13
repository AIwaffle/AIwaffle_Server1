def test_total(client):
    response1 = client.get(
        "/api/statistics/total"
    )
    response2 = client.get(
        "/api/statistics/total"
    )
    assert int(response1.data) + 1 == int(response2.data)
