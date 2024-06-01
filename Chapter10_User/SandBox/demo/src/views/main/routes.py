from flask import render_template, Blueprint
from flask_login import current_user
from os import path

from src.models.product import UserProduct
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@main_blueprint.route("/about")
def about():
    return render_template("about.html")