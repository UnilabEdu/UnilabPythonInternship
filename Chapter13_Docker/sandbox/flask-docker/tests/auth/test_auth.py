from flask_login import current_user
from src.models.user import User

def test_admin_redirect(client):
    response = client.get("/admin", follow_redirects=True)
    assert response.request.path == "/login"


def test_login_page(client):
    response = client.get("/login")

    assert response.status_code == 200

    with client:
        response = client.post("/login", data={"login": "admin@mail.com", "password": "password123"}, follow_redirects=True)
        assert current_user.is_authenticated


def test_failed_register(client):

    response = client.get("/register")
    assert response.status_code == 200

    with client:
        response = client.post("/register", data={"email": "mymail@yahoo.com", "username": "testuser123",
                                                  "password": "password1234", "confirm_password": "password12345"}, follow_redirects=True)
        assert b"Passwords must match" in response.data


def test_register_success(client):

    response = client.get("/register")
    assert response.status_code == 200

    with client:
        response = client.post("/register", data={"email": "mymail@yahoo.com", "username": "testuser123",
                                                  "password": "password1234", "confirm_password": "password1234"}, follow_redirects=True)

        registered_user = User.query.filter_by(email="mymail@yahoo.com").first()
        assert response.request.path == "/login"
