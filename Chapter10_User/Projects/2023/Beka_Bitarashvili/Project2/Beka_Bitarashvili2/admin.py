from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)
login_manager = LoginManager(app)


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index2'))


admin = Admin(app, index_view=MyAdminIndexView(), template_mode='bootstrap4')


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.Unicode(100))
    username = db.Column(db.String(100))


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    direction = db.Column(db.String(30))
    level = db.Column(db.Numeric(100))


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    databases = db.Column(db.String(50))


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index2'))


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Developer, db.session))
admin.add_view(MyModelView(Skill, db.session))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')


@app.route('/')
def index2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
