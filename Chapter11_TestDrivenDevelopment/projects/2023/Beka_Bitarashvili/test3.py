import pytest
from admin import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 200
    assert b'main page' in response.data


def test_protected_routes_without_login(client):
    response = client.get('/admin')
    assert response.status_code == 308
    assert response.location == 'http://localhost/admin/'


def test_protected_routes_with_login(client):
    client.post('/login', data={'username': 'bekabitara', 'password': '12345678'})
    response = client.get('/admin')
    assert response.status_code == 308
