from flask import Blueprint, render_template, redirect, url_for
from app.Players.forms import AddForm, DeleteForm
from app.models import Team, Players



students_blueprint = Blueprint('players',
                               __name__,
                               template_folder='templates/players'
                               )


# server:port/blueprint_prefix/list
@students_blueprint.route('/')
def list():
    return render_template('home.html')


@students_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.submit.data and form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        team = form.team.data
        item = Players()

        item.create(name=name, surname=surname, team=team)
        return redirect(url_for('players.list_items'))

    return render_template('players.html', form=form)

@students_blueprint.route('/list', methods=['GET', 'POST'])
def list_items():
    team = Players.query.all()
    return render_template('list.html', team = team)

@students_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_item():
    form = DeleteForm()

    if form.validate_on_submit():

        item_id = form.id.data
        item = Players.query.get(item_id)
        if item != None:
            item.delete()
            return redirect(url_for('players.list_items'))
        else:
            return "error, this id is not here "

    return render_template('delete.html', form=form)

@students_blueprint.route('/update', methods=['GET', 'POST'])
def update_item():
    form = AddForm()

    if form.validate_on_submit():


        name = form.name.data
        surname = form.surname.data
        team = form.team.data
        id = form.id.data

        item = Players.query.get(id)
        item.update(name=name, surname=surname, team=team)
        return redirect(url_for('players.list_items'))

    return render_template('update.html', form=form)



