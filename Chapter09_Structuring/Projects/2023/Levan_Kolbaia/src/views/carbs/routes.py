from flask import render_template, Blueprint
from os import path
from uuid import uuid4

#from src.config import Config

carbs_blueprint = Blueprint("carbs", __name__ template_folder="Templates/carbs")

@carbs_blueprint.blueprint.route("/carbs")
def carbset():
    return render_template("/Carbset.html")