from flask import Blueprint, render_template
from src.models.cinema import Actor, Film

actors_blueprint = Blueprint("actor", __name__, template_folder="templates")


@actors_blueprint.route("/actors")
def actors():
    actors = Actor.query.all()
    films = Film.query.all()
    return render_template("actors/actors.html", actors=actors, films=films)