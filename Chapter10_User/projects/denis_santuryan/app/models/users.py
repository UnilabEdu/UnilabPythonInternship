from app import db
from app.tools.format_dob import calculate_age
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False, index=True)
    name_first = db.Column(db.String)
    name_last = db.Column(db.String)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    phone = db.Column(db.String)
    sex = db.Column(db.String)
    dob = db.Column(db.Date)
    password = db.Column(db.String(255))
    age = db.Column(db.Integer)
    picture = db.Column(db.String)
    post = db.relationship('PostsModel', backref='usermodel', uselist=False)

    def __init__(self, username, name_first, name_last, email, phone, dob, sex, password, age=None, picture=None):
        self.username = username
        self.name_first = name_first
        self.name_last = name_last
        self.email = email
        self.phone = phone
        self.dob = dob
        self.sex = sex
        self.password = generate_password_hash(password)
        self.age = calculate_age(dob)
        self.picture = picture

    def __repr__(self):
        return f'ID: {self.id}. {self.username}'

    def check_password(self, password_raw):
        return check_password_hash(self.password, password_raw)

    @classmethod
    def find_by_username(cls, temp_username):
        return cls.query.filter_by(username=temp_username).first()

    @classmethod
    def find_by_email(cls, temp_email):
        return cls.query.filter_by(email=temp_email).first()


# later check if I need the 'try' part. if yes, define the exact exception
@login_manager.user_loader
def load_user(user_id):
    try:
        return UserModel.query.get(user_id)
    except:
        pass
