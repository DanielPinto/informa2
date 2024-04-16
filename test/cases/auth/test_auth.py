import pytest
from app.models import Item
from app.cases.auth.login import getToken



async def test_get_token():
    item = Item(username='99810344@ambev.com.br', password='123456')
    response = await getToken(item=item)
    assert "access_token" in response
    assert type(response['access_token']) == str
    assert len(response['access_token']) > 50




async def test_error_credentials_get_token():
    item = Item(username='99810345@ambev.com.br', password='1234')
    response = await getToken(item=item)
    assert "error" in response
    assert "error_description" in response
    assert response['error_description'] == "Invalid user credentials"