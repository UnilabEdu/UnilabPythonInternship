from flask_login import current_user

def test_index(client):
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200
def test_add_product_unauthorized(client):
    response = client.get("/add_product", follow_redirects=True)
    assert response.request.path == "/login"
    assert b"Please log in to access this page." in response.data

def test_login(client):
    with client:
        client.post("/login", data={"username": "admin", "password": "password123"})
        assert current_user.is_authenticated

        response = client.get("/add_product", follow_redirects=True)
        assert response.request.path == "/add_product"
        assert b"Add New Product" in response.data



