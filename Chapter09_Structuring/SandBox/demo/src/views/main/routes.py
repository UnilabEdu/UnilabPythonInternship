from flask import render_template, Blueprint, flash
from os import path
from uuid import uuid4

from src.views.main.forms import RegisterForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_picture.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = path.join(Config.UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("index.html", user_type="admin", form=form)


@main_blueprint.route("/about")
def about():
    return render_template("about.html")