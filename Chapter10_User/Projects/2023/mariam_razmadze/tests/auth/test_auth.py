from teamapp.models.user import User
from flask_login import current_user

def test_admin_redirect(client):
    response=client.get("/admin", follow_redirects=True)
    assert response.request.path == '/login'


def test_user_register(client, app):
    response=client.get("/register")
    assert response.status_code==200
    

    with client:
        response=client.post('/register', data={'name': 'phoebe', 'password': 'asdf'}, follow_redirects=True)
        assert response.request.path == '/login'
        registered_user=User.query.filter_by(name='phoebe').first()
        assert registered_user


def test_login(client):
    response=client.get('/login')
    assert response.status_code == 200

    with client:
        client.post('/login', data={'name': 'lalo', 'password': 'asdf'})
        assert current_user.is_authenticated



def test_asking_questions(client):
    assert client.get('/login').status_code == 200
    response=client.get('/', follow_redirects=True)
    assert b'What kind of bear is best?' in response.data



