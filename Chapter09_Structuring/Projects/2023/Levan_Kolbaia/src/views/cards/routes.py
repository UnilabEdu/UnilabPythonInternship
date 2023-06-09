from flask import render_template, Blueprint
from os import path
from uuid import uuid4

#from src.config import Config

cards_blueprint = Blueprint("cards", __name__ template_folder="Templates/cards")

@cards_blueprint.blueprint.route("/cards")
def macronutrients():
    return render_template("/Cards.html", card_list=cards)

cards = [
    {"name": "Buckwheat(100g)",
     "description": '350 k/cal'},
    {"name": "Rice(100g)",
     "description": "300 k/cal"}
]