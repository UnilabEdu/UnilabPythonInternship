from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user

from src.config import Config

from os import path


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "profile")
profile_blueprint = Blueprint("profile", __name__, template_folder=TEMPLATES_FOLDER)


@profile_blueprint.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)