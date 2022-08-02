from flask_login import current_user
import sys

def test_redirect(client):
    response = client.get('/home', follow_redirects=True)
    assert response.request.path == '/users/login'

def test_login(client):
    assert client.get('/users/login').status_code == 200

    with client:
        client.post('/users/login', data={'email':'mail@gmail.com', 'password':'123'})

        assert current_user.is_authenticated

def test_failed_register(client):
    assert client.get('/users/registration').status_code == 200

    response = client.post('/users/registration', data={'email':'random@gmail.com', 'username':'random', 'password':'1234', 'pass_confirm':'123456'}, follow_redirects=True)
    assert response.request.path == '/users/registration'



def test_succesfull_register(client):
    assert client.get('/users/registration').status_code == 200

    response = client.post('/users/registration', data={'email':'random@gmail.com', 'username':'randomm', 'password':'1234', 'pass_confirm':'1234'}, follow_redirects=True)
    assert response.request.path == '/users/login'
