from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)

admin = Admin(app, template_mode='bootstrap4')


class User(db.Model):
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


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Developer, db.session))
admin.add_view(ModelView(Skill, db.session))


@app.route('/')
def index2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
