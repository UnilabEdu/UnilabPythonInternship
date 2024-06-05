from flask import render_template, Blueprint
from flask_login import login_required

from src.config import Config

from os import path


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "profile")
profile_blueprint = Blueprint("profile", __name__, template_folder=TEMPLATES_FOLDER)


@profile_blueprint.route("/profile")
@login_required
def profile():
    return render_template("profile.html")