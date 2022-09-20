import json
import pytest

mock_user = {
    "username": "johndoe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "kissa123",
}

def test_user_register(test_app_with_db):
    response = test_app_with_db.post("/users", data=json.dumps(mock_user))
    assert response.status_code == 201

