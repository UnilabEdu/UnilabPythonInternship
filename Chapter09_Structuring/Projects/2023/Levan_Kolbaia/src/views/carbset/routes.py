from flask import render_template, Blueprint
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "carbset")
carbset_blueprint = Blueprint("carbset",__name__, template_folder=TEMPLATES_FOLDER)


@carbset_blueprint.route("/carbs")
def carbset():
    return render_template("Carbset.html")
