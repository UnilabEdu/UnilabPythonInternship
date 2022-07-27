from flask import Blueprint, render_template, redirect, url_for

from app.models import Student
from app.students.forms import AddForm


students_blueprint = Blueprint('students',
                               __name__,
                               template_folder='templates/students'
                               )


# server:port/student/add
@students_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_student = Student(name)
        new_student.save_to_db()
        return redirect(url_for('students.roll'))
    return render_template('add.html', form=form)


# server:port/blueprint_prefix/list
@students_blueprint.route('/')
def roll():
    students = Student.query.all()
    return render_template('list.html', students=students)


# # server:port/blueprint_prefix/delete
# @students_blueprint.route('/delete')
# def delete():
#     pass
