from flask import Blueprint, render_template

from app.auth.forms import SignInForm


main_blueprint = Blueprint(
		'main',
		__name__,
		template_folder='templates/main'
	)


@main_blueprint.route('/')
def index():
	form = SignInForm()
	return render_template('index.html', form=form)
