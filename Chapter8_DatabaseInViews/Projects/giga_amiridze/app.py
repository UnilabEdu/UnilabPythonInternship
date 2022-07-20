from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from resources.pages import nav_bar_pages
from forms import AddForm, DeleteForm

app = Flask(__name__)
db = SQLAlchemy(app)
Migrate(app, db)

app.config['SECRET_KEY'] = 'my_secret_key'

base_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'data.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, db_name)}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    @classmethod
    def read(cls, first_name):
        return cls.query.filter_by(first_name=first_name).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Student: {self.first_name.capitalize()} {self.last_name.capitalize()}"

@app.route('/')
def home():
    return render_template('home.html', pages=nav_bar_pages)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data

        student = Student()
        student.create(first_name=first_name, last_name=last_name, age=age, email=email, commit=True)
        return redirect(url_for('students_list'))

    return render_template('add.html', pages=nav_bar_pages, form=form)

@app.route('/students_list', methods=['GET', 'POST'])
def students_list():
    db_list = Student.query.all()
    return render_template('list.html', pages=nav_bar_pages, students_list=db_list)

@app.route('/update', methods=['GET', 'POST'])
def update():
    form = AddForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data

        student = Student.read(first_name=first_name)
        student.create(first_name=first_name, last_name=last_name, age=age, email=email, commit=True)
        return redirect(url_for('students_list'))

    return render_template('update.html', pages=nav_bar_pages, form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        student_id = form.student_id.data
        student = Student.query.get(student_id)
        student.delete_from_db()
        return redirect(url_for('students_list'))

    return render_template('delete.html', pages=nav_bar_pages, form=form)

if __name__ == '__main__':
    app.run(port=7777, debug=True)
