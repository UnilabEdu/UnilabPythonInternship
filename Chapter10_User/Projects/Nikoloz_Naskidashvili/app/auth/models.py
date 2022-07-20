from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'auth_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    hashed_password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
