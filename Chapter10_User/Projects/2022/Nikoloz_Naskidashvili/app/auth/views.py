from flask import Blueprint, render_template, redirect, url_for, flash, abort, request

from flask_login import login_user, login_required, logout_user

from app.extensions import db
from app.auth.models import User
from app.auth.forms import SignInForm, SignUpForm


auth_blueprint = Blueprint(
		'auth',
		__name__,
		template_folder='templates/auth',
		url_prefix='/auth'
	)


@auth_blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	form = SignUpForm()

	if form.validate_on_submit():
		user = User(username=form.username.data, password=form.password1.data)

		db.session.add(user)
		db.session.commit()
		flash('Successfully signed up', 'success')
		return redirect(url_for('auth.sign_in'))

	return render_template('sign-up.html', form=form)


@auth_blueprint.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
	form = SignInForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()

		if user is not None and user.check_password(form.password.data):
			if form.remember.data:
				login_user(user, remember=True)
			else:
				login_user(user)
			flash('Successfully signed in', 'success')

			next_url = request.args.get('next')

			if next_url is None or not next_url[0] == '/':
				next_url = url_for('blog.blog')

			return redirect(next_url)
		else:
			flash('Sign in failed, try checking your username and password', 'danger')
	return redirect(url_for('main.index'))


@auth_blueprint.route('/sign-out')
@login_required
def sign_out():
	logout_user()
	flash('Successfully signed out', 'success')
	return redirect(url_for('main.index'))
