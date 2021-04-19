from flask import Blueprint, redirect, url_for, render_template, flash
from app.models import Student, Tutor
from app.common.forms import DeleteForm, ChoiceForm
from app.pages_list import nav_bar_pages_list

common_blueprint = Blueprint('common',
                             __name__,
                             template_folder='templates/common'
                             )


@common_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = ChoiceForm()
    if form.validate_on_submit():
        choice = form.choice.data
        if choice == "student":
            return redirect(url_for('students.register_student'))
        else:
            return redirect(url_for('tutors.register_tutor'))

    return render_template("registration.html", pages=nav_bar_pages_list, form=form)


@common_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_user():
    form = DeleteForm()
    choice = form.choice.data

    if form.validate_on_submit():
        if choice == "student":
            item_id = form.id.data
            item = Student.query.get(item_id)
            item.delete_student()

            flash("The user was successfully deleted!")
            return redirect(url_for('common.delete_user'))
        else:
            item_id = form.id.data
            item = Tutor.query.get(item_id)
            item.delete_tutor()

            flash("The user was successfully deleted!")
            return redirect(url_for('common.delete_user'))

    return render_template('delete.html', pages=nav_bar_pages_list, form=form)
