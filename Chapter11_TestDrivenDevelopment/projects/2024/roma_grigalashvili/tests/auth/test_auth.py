from flask_login import current_user


def test_unauthenticated(client):
    response = client.get("/profile", follow_redirects=True)
    assert response.request.path == "/login"
    
def test_login(client):
    # Make a request to the login page
    response = client.get("/login")
    assert response.status_code == 200

    # Submit login form
    with client:
        response = client.post("/login", data={"email": "roma.grigalashvili@iliauni.edu.ge", "password": "Grigalash1"}, follow_redirects=True)
        assert response.status_code == 200
        assert current_user.is_authenticated

