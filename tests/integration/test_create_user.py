def test_create_user(client):
    response = client.get("/api/user/get-users")
    assert response.status_code == 200
    assert response.json() == []

    response = client.post(
        "/api/user/create-user",
        json={"email": "test@example.com", "full_name": "Full Name Test"},
    )
    assert response.status_code == 200

    response = client.get(f"/api/user/get-user?id={response.json().get('id')}")
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json().get("id"),
        "email": "test@example.com",
        "full_name": "Full Name Test",
    }

    response = client.get("/api/user/get-users")
    assert response.status_code == 200
    assert len(response.json()) == 1
