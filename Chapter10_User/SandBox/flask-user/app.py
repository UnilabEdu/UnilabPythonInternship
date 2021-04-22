import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter, UserManager, UserMixin, login_required
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = "MySecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


@app.route('/')
def home():
    return '<h1>მოგესალმებით თავ-ფურცელზე</h>'


@app.route('/profile')
@login_required
def profile():
    return '<h1>მოგესალმებით მომხმარებლის გვერდზე</h>'


if __name__ == '__main__':
    app.run(debug=True)
