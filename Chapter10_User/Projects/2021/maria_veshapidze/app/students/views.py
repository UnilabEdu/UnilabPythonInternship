from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user
from app.models import Student
from app.students.forms import EmailFormStudent, LoginFormStudent
from app.pages_list import nav_bar_pages_list
from app import db

students_blueprint = Blueprint('students',
                               __name__,
                               template_folder='templates/students'
                               )


@students_blueprint.route('/register_student', methods=['GET', 'POST'])
def register_student():
    form = EmailFormStudent()

    if form.validate_on_submit():
        student = Student(username=form.username.data,
                          email=form.email.data,
                          password=form.password.data,
                          tutor_id=form.tutor_id.data)

        student.add_student()

        flash(f"{student.username}, You are successfully registered, please log in!")
        return redirect(url_for('students.student_login'))

    return render_template("register_student.html", form=form)


@students_blueprint.route('/students_list', methods=['GET', 'POST'])
def students_list():
    db_list = Student.query.all()
    return render_template('list.html', db_list=db_list, pages=nav_bar_pages_list)


@students_blueprint.route('/student_login', methods=['GET', 'POST'])
def student_login():
    form = LoginFormStudent()
    if form.validate_on_submit():
        user = Student.find_by_email(form.email.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("You are successfully logged in")

            next = request.args.get('next')

            if next is None:
                next = url_for('home')

            return redirect(next)

    return render_template('student_login.html', form=form, pages=nav_bar_pages_list)
