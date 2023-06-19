from flask import render_template, Blueprint
from os import path
from src.models.users import User
from src.views.main.forms import RegisterForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def nutrition():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.create()

    else:
        print(form.errors)

    return render_template('Nutrition1010.html', form=form)
