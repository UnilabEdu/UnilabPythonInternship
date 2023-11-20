from flask import render_template, Blueprint, redirect, url_for

from src.views.auth.forms import RegisterForm



auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))

    return render_template('auth/register.html', form=form)