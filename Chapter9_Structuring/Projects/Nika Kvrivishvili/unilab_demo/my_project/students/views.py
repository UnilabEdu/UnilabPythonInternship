from flask import Blueprint, render_template, redirect, url_for
from my_project.students.forms import AddForm, DelForm
from my_project.programs.models import Program
from my_project.students.models import Student


students_blueprint = Blueprint('students',
                               __name__,
                               template_folder='templates/students')


@students_blueprint.route('/')
@students_blueprint.route('/add', methods=['GET', 'POST'])
def add_student():
    form = AddForm()
    form.program_id.choices = Program.get_choices()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        program_id = form.program_id.data

        user = Student(name, email, program_id)
        user.create()

        form.name.data = ''
        form.email.data = ''

        redirect(url_for('students.add_student'))

    return render_template('add.html', form=form)


@students_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_student():
    form = DelForm()

    if form.validate_on_submit():
        user_id = form.id.data

        user_by_id = Student.get_by_id(user_id)
        user_by_id.delete()

        form.id.data = ''

        redirect(url_for('students.delete_student'))

    return render_template('delete.html', form=form)
