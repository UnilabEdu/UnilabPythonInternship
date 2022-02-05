import os
from forms import AddForm, DelForm, AddFormAdmin
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Program(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    students = db.relationship('Student', backref='student')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    program_id = db.Column(db.Integer, db.ForeignKey(Program.id))

    def __init__(self, name, email, program_id):
        self.name = name
        self.email = email
        self.program_id = program_id

    def __repr__(self):
        return self.name

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


db.create_all()


@app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        program_id = form.program_id.data

        user = Student(name, email, program_id)
        db.session.add(user)
        db.session.commit()

        form.name.data = ''
        form.email.data = ''

        redirect(url_for('add_student'))

    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete_student():
    form = DelForm()

    if form.validate_on_submit():
        user_id = form.id.data

        user_by_id = Student.query.get(user_id)
        db.session.delete(user_by_id)
        db.session.commit()

        form.id.data = ''

        redirect(url_for('delete_student'))

    return render_template('delete.html', form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AddFormAdmin()

    if form.validate_on_submit():
        program = form.program.data

        add_program = Program(program)

        db.session.add(add_program)
        db.session.commit()

        form.program.data = ''

        redirect(url_for('admin'))

    return render_template('admin.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
