from flask import Blueprint, redirect, url_for, render_template, flash
from app.models import Student
from app.students.forms import EmailFormStudent
from app.pages_list import nav_bar_pages_list

students_blueprint = Blueprint('students',
                               __name__,
                               template_folder='templates/students'
                               )


@students_blueprint.route('/register_student', methods=['GET', 'POST'])
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
        return redirect(url_for('students.register_student'))

    return render_template("register_student.html", form=form, email=email, password=password)


@students_blueprint.route('/students_list', methods=['GET', 'POST'])
def students_list():
    db_list = Student.query.all()
    return render_template('list.html', db_list=db_list, pages=nav_bar_pages_list)
