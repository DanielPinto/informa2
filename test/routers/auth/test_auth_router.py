from fastapi.testclient import TestClient
from fastapi import status 

from app.main import app

client = TestClient(app)
#headers = {"Authorization": "Bearer token"}
#client.headers = headers


def test_auth_get_token_route():
    body = {
        "username": "99810344@ambev.com.br",
        "password": "123456"
    }
    response = client.post('/login', json=body)
    assert response.status_code == status.HTTP_200_OK
    




def test_auth_error_credentials_get_token_route():
    body = {
        "username": "99810345@ambev.com.br",
        "password": "1234"
    }
    response = client.post('/login', json=body)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "error_description" in data
    assert data['error_description'] == "Invalid user credentials"
    

def test_auth_error_field_required_get_token_route():
    body = {
        "username": "99810345@ambev.com.br"
    }
    response = client.post('/login', json=body)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    data = response.json()
    assert "msg" in data['detail'][0]
    assert "Field required" in data['detail'][0]['msg']