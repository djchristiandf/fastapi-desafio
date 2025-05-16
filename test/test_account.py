def test_create_account(client):
    response = client.post(
        "/accounts/",
        json={"user_id": 1, "balance": 100.0}
    )
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_accounts(client, auth_headers):
    response = client.get("/accounts/?limit=10", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)