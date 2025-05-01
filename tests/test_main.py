from fastapi.testclient import TestClient
from interview.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Capgemini Interview Project API!"}

def test_create_user():
    user_data = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    if users:
        assert "name" in users[0]
        assert "email" in users[0]
        assert "id" in users[0]
