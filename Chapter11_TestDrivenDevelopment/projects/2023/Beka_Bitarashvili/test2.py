import pytest
from flask import Flask, url_for
from admin import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_web_title(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<title>Admin-Home Page</title>" in response.data


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"hello" in response.data


def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"logged in" in response.data
