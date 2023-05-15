from flask import render_template, redirect, url_for
from forms8 import UserForm, DeleteForm
from models import app, db, User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register_user', methods=['GET', 'POST'])
def register():
    myform = UserForm()

    if myform.validate_on_submit():
        username = myform.username.data
        email = myform.email.data
        password = myform.password.data
        experience = myform.experience.data
        account_type = myform.account_type.data
        user = User()
        user.create(username=username, email=email, password=password, experience=experience, account_type=account_type, commit=True)
        return redirect(url_for('registered'))
    return render_template("register.html", form=myform)


@app.route('/list', methods=['GET', 'POST'])
def list_users():
    db_list = User.query.all()
    return render_template('list.html', list_users=db_list)


@app.route('/update', methods=['GET', 'POST'])
def update_users():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        experience = form.experience.data
        account_type = form.account_type.data

        item = User.read(username=username)
        item.update(username=username, email=email, experience=experience, account_type=account_type, commit=True)
        return redirect(url_for('list_items'))

    return render_template('update.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete_users():
    form = DeleteForm()
    db_list = User.query.all()

    if form.validate_on_submit():
        user_id = form.id.data
        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('list_users'))

    return render_template('delete.html', list_users=db_list, form=form)


@app.route('/registered', methods=['GET', 'POST'])
def registered():
    return render_template('registered.html')


if __name__ == '__main__':
    app.run(debug=True)
