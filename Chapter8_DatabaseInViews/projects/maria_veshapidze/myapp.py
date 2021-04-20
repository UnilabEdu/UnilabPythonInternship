from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from forms import EmailFormStudent, EmailFormTutor, ChoiceForm, DeleteForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Tutor(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    subject = db.Column(db.String)

    student = db.relationship('Student', backref='Tutor', uselist=False)

    def __init__(self, name, email, password, subject):
        self.name = name
        self.email = email
        self.password = password
        self.subject = subject

    def add_tutor(self):
        db.session.add(self)
        db.session.commit()

    def delete_tutor(self):
        db.session.delete(self)
        db.session.commit()


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

    def __init__(self, name, email, password, tutor_id):
        self.name = name
        self.email = email
        self.password = password
        self.tutor_id = tutor_id

    def add_student(self):
        db.session.add(self)
        db.session.commit()

    def delete_student(self):
        db.session.delete(self)
        db.session.commit()


nav_bar_pages_list = (
    ("home", "Home",),
    ("about", "About us"),
    ("contact", "Contact Info"),
    ("registration", "Registration"),
    ("delete_user", "Delete"),
    ("students_list", "Students' list")
)


@app.route('/')
@app.route('/<guestname>')
def home(guestname=None):
    return render_template("home_page.html", name=guestname, pages=nav_bar_pages_list)


@app.route('/about_us')
def about():
    return render_template("about_us.html", pages=nav_bar_pages_list)


@app.route('/contact_info')
def contact():
    return render_template("contact_info.html", pages=nav_bar_pages_list)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = ChoiceForm()
    if form.validate_on_submit():
        choice = form.choice.data
        if choice == "student":
            return redirect(url_for('register_student'))
        else:
            return redirect(url_for('register_tutor'))

    return render_template("registration.html", pages=nav_bar_pages_list, form=form)


@app.route('/register_student', methods=['GET', 'POST'])
def register_student():
    email = None
    password = None

    form = EmailFormStudent()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        tutor_id = form.tutor_id.data

        item = Student(name, email, password, tutor_id)
        item.add_student()

        flash(f"{name}, You were successfully registered!")
        return redirect(url_for('register_student'))

    return render_template("register_student.html", pages=nav_bar_pages_list, form=form, email=email, password=password)


@app.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    email = None
    password = None

    form = EmailFormTutor()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        subject = form.subject.data

        item = Tutor(name, email, password, subject)
        item.add_tutor()

        flash(f"{name}, You were successfully registered!")
        return redirect(url_for('register_tutor'))

    return render_template("register_tutor.html", pages=nav_bar_pages_list, form=form, email=email, password=password)


@app.route('/students_list', methods=['GET', 'POST'])
def students_list():
    db_list = Student.query.all()
    return render_template('list.html', pages=nav_bar_pages_list, db_list=db_list)


@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    form = DeleteForm()
    choice = form.choice.data

    if form.validate_on_submit():
        if choice == "student":
            item_id = form.id.data
            item = Student.query.get(item_id)
            item.delete_student()

            flash("The user was successfully deleted!")
            return redirect(url_for('delete_user'))
        else:
            item_id = form.id.data
            item = Tutor.query.get(item_id)
            item.delete_tutor()

            flash("The user was successfully deleted!")
            return redirect(url_for('delete_user'))

    return render_template('delete.html', pages=nav_bar_pages_list, form=form)


if __name__ == '__main__':
    app.run(port=8085, debug=True)
