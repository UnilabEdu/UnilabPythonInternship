from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Coach
from app.coaches.forms import AddForm, DeleteForm

coaches_blueprint = Blueprint('coaches',
                              __name__,
                              template_folder='templates/coaches')



@coaches_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    my_form = AddForm()

    if my_form.validate_on_submit():
        name = my_form.name.data
        age = my_form.age.data
        coach = Coach()
        coach.create(name=name, age=age)
        message = "Coach Added"
        flash(message)
        return redirect(url_for('coaches.read'))
    return render_template('create.html', form=my_form)

@coaches_blueprint.route('/read')
def read():

    coaches = Coach.read_all()

    return render_template('read.html', my_coaches=coaches)

@coaches_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    my_form = AddForm()
    coaches = Coach.read_all()

    if my_form.validate_on_submit():

        name = my_form.name.data
        age = my_form.age.data
        coach = Coach.query.filter_by(name=name).first()
        if coach is not None:
            message = "Coach Updated"
            flash(message)
            coach.update(age=age)
            return redirect(url_for('coaches.read'))
        else:
            message = f"There is no Coach named: {name}, Try again."
            flash(message)
            return redirect(url_for('coaches.update'))

    return render_template('update.html', my_coaches=coaches, form=my_form)

@coaches_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    my_form = DeleteForm()
    coaches = Coach.read_all()
    if my_form.validate_on_submit():
        name = my_form.name.data
        coach = Coach.query.filter_by(name=name).first()
        if coach is not None:
            message = "Coach Deleted"
            flash(message)
            coach.delete()

        else:
            message = f"There is no Coach named: {name}, Try again."
            flash(message)
            return redirect(url_for('coaches.delete'))
        return redirect(url_for('coaches.read'))

    return render_template('delete.html', form =my_form, my_coaches=coaches)