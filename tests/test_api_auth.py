def test_register(client):
    # No data
    response = client.post(
        "/api/auth/register",
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    # Partial data
    response = client.post(
        "/api/auth/register", json={"username": "test_u4"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    response = client.post(
        "/api/auth/register", json={"password": "a"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    # Regular registration
    response = client.post(
        "/api/auth/register", json={"username": "test_u4", "password": "a"},
    )
    assert response.status_code == 200
    assert response.json["success"]

    # Duplicate
    response = client.post(
        "/api/auth/register", json={"username": "test_u4", "password": "a"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "already" in response.json["reason"]


def test_login(client):
    response = client.post(
        "/api/auth/register", json={"username": "test_u5", "password": "a"},
    )
    assert response.status_code == 200
    assert response.json["success"]
    uuid = response.json["uuid"]

    # No data
    response = client.post(
        "/api/auth/login",
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    # Partial data
    response = client.post(
        "/api/auth/login", json={"username": "test_u5"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    response = client.post(
        "/api/auth/login", json={"password": "a"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "required" in response.json["reason"]

    # Does not exist
    response = client.post(
        "/api/auth/login", json={"username": "username", "password": "a"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "exist" in response.json["reason"]

    # Wrong record
    response = client.post(
        "/api/auth/login", json={"username": "test_u5", "password": "b"},
    )
    assert response.status_code == 200
    assert not response.json["success"]
    assert "record" in response.json["reason"]

    # Regular login
    response = client.post(
        "/api/auth/login", json={"username": "test_u5", "password": "a", "session": 1},
    )
    assert response.status_code == 200
    assert response.json["success"]

    response = client.get(
        "/auth/current",
    )
    assert response.status_code == 200
    assert response.json["uuid"] == uuid
    assert response.json["username"] == "test_u5"
