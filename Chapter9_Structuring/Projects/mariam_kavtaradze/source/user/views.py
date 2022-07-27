from flask import Blueprint, render_template, url_for, redirect
from source.user.forms import BaseForm, GetForm
from source.user.models import User

user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates/users')


@user_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    form = BaseForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        experience = form.experience.data
        account_type = form.account_type.data
        user = User()
        user.create(username=username,
                    email=email,
                    password=password,
                    experience=experience,
                    account_type=account_type,
                    commit=True)
        return redirect(url_for('user.read_all'))
    return render_template("create.html", form=form)


@user_blueprint.route('/read_all', methods=['GET'])
def read_all():
    all_users = User.read_all()
    return render_template('read_all.html', all_users=all_users)


@user_blueprint.route('/read_one', methods=['GET', 'POST'])
def read_one():
    form = GetForm()
    if form.validate_on_submit():
        user_id = form.id.data
        user = User.read_one(user_id)
        return render_template('read_one.html', user=user)
    return render_template('get_user.html', form=form)


@user_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    get_form = GetForm()
    all_users = User.read_all()
    if get_form.validate_on_submit():

        user = User.read_one(get_form.id.data)
        form = BaseForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            experience = form.experience.data
            account_type = form.account_type.data
            user.update(username=username,
                        email=email,
                        experience=experience,
                        account_type=account_type,
                        commit=True)
            return redirect(url_for('user.read_all'))
        return render_template('update.html', user=user, form=form)
    return render_template('get_user.html', all_users=all_users, form=get_form)


@user_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = GetForm()
    all_users = User.read_all()
    if form.validate_on_submit():
        user_id = form.id.data
        user = User.query.get(user_id)
        user.delete()
        return redirect(url_for('user.read_all'))
    return render_template('get_user.html', all_users=all_users, form=form)




