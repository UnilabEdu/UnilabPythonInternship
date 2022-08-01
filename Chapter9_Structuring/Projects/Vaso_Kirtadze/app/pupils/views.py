from flask import render_template, redirect, url_for, flash, Blueprint
from app.models import Pupil, Coach

from app.pupils.forms import AddForm, DeleteForm

pupils_blueprint = Blueprint('pupils',
                             __name__,
                             template_folder='templates/pupils')


@pupils_blueprint.route('/create', methods=['GET', 'POST'])
def create_pupil():
    my_form = AddForm()

    if my_form.validate_on_submit():
        name = my_form.name.data
        is_active = my_form.is_active.data
        coach_id = my_form.coach_id.data
        coahces = Coach.read_all()
        coahce_id_s = [item.id for item in coahces]

        if coach_id in coahce_id_s:
            pupil = Pupil()
            pupil.create(name=name, is_active=is_active, coach_id=coach_id)
            message = "Pupil Added"
            flash(message)
            return redirect(url_for('pupils.read_pupil'))
        else:
            message = "There is no coach with that ID"
            flash(message)
            return redirect(url_for('pupils.create_pupil'))

    return render_template('create_pupil.html', form=my_form)


@pupils_blueprint.route('/read', methods=['GET', 'POST'])
def read_pupil():

    pupils = Pupil.read_all()

    return render_template('read_pupil.html', my_pupils=pupils)


@pupils_blueprint.route('/update', methods=['GET', 'POST'])
def update_pupil():
    my_form = AddForm()
    pupils = Pupil.read_all()

    if my_form.validate_on_submit():
        name = my_form.name.data
        is_active = my_form.is_active.data
        coach_id = my_form.coach_id.data
        coahces = Coach.read_all()
        coahce_id_s = [item.id for item in coahces]

        pupil = Pupil.query.filter_by(name=name).first()
        if pupil is not None and coach_id in coahce_id_s:
            message = "Pupil Updated"
            flash(message)
            pupil.update(is_active=is_active, coach_id=coach_id)
            return redirect(url_for('pupils.read_pupil'))
        else:
            message = "Either there is no coach with this ID or there is no pupil with this name"
            flash(message)
            return redirect(url_for('pupils.update_pupil'))

    return render_template('update_pupil.html', my_pupils=pupils, form=my_form)


@pupils_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_pupil():
    my_form = DeleteForm()
    pupils = Pupil.read_all()
    if my_form.validate_on_submit():
        name = my_form.name.data

        pupil = Pupil.query.filter_by(name=name).first()

        if pupil:
            message = "Pupil Deleted"
            flash(message)
            pupil.delete()
            return redirect(url_for('pupils.read_pupil'))
        else:
            message = "There is no pupil with this name"
            flash(message)
            return redirect(url_for('pupils.delete_pupil'))

    return render_template('delete_pupil.html', my_pupils=pupils, form=my_form)