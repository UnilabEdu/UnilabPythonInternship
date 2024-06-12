from src.models import User, Role

def test_user_creation(app):
    with app.app_context():
        user = User(username="testuser", email="testuser@example.com", password="testpassword")
        user.create()

        test_user = User.query.filter_by(email="testuser@example.com").first()
        assert test_user is not None
        assert test_user.username == "testuser"
        assert test_user.email == "testuser@example.com"

def test_password_hashing(app):
    with app.app_context():
        password = "TestPassword"
        user = User(username="testuser", email="testuser@example.com", password=password)
        user.create()

        test_user = User.query.filter_by(email="testuser@example.com").first()
        assert test_user is not None
        assert test_user.check_password(password) == True
        assert test_user.check_password("WrongPassword") == False

def test_default_role(app):
    with app.app_context():
        role = Role(name="default")
        role.create()

        user = User(username="testuser", email="testuser@example.com", password="TestPassword1", role_id=4)
        user.create()

        test_user = User.query.filter_by(email="testuser@example.com").first()
        assert test_user is not None
        assert test_user.role is not None
        assert test_user.role.name == "default"
