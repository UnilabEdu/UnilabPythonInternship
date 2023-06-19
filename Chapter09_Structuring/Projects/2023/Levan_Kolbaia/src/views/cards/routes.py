from flask import render_template, Blueprint
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "cards")
cards_blueprint = Blueprint("cards", __name__, template_folder=TEMPLATES_FOLDER)


@cards_blueprint.route("/cards")
def macronutrients():
    return render_template("Cards.html", card_list=cards)


cards = [
    {"name": "Buckwheat(100g)",
     "description": '350 k/cal'},
    {"name": "Rice(100g)",
     "description": "300 k/cal"}
]
