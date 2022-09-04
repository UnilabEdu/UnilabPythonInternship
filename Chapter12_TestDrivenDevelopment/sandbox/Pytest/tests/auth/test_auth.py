from flask_login import current_user


def test_redirect(client):
    response = client.get('/profile', follow_redirects=True)
    assert response.request.path == '/login'


def test_login(client):
    assert client.get('/login').status_code == 200

    with client:
        client.post('/login', data={'login': 'user', 'password': 'password123'})
        assert current_user.is_authenticated


def test_failed_register(client):
    assert client.get('/register').status_code == 200
    response = client.post('/register', data={'username': "Temo", "email": "something555@mail.com",
                                              "password": "password5", "confirm_password": "password7"}, follow_redirects=True)

    assert b"Passwords must match" in response.data


def test_successful_register(client):
    assert client.get('/register').status_code == 200
    response = client.post('/register', data={'username': "Temo", "email": "something555@mail.com",
                                              "password": "password5", "confirm_password": "password5"}, follow_redirects=True)

    assert response.request.path == '/'
