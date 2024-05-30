from flask_login import current_user

def test_add_product(client):
    response = client.get("/admin", follow_redirects = True)
    assert response.request.path == "/login/"




def test_index(client):
    response = client.get("/")
    assert response.status_code == 200



def test_wrong_password(client):
    with client:
        response = client.post("/login",
                               data={"username": "admin", "password" : "admin12365"},
                               follow_redirects = True)
        assert b"Invalid username or password" in response.data


def test_wrong_emai(client):
    with client:
        response = client.post("/contact", data = {"name": "mea", "email" : "meafn", "phone":"573",
                                            "company" : "afg", "message": "cat"},  follow_redirects = True)
        assert b"Invalid email or phone" in response.data

def test_correct_info(client):
    with client:
        response = client.post("/contact", data = {"name": "mea", "email" : "mariamiii1999@gmail.com", "phone":"598745620",
                                            "company" : "afg", "message": "cat"}, follow_redirects = True)
        assert response.request.path == "/"