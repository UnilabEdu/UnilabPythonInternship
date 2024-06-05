from flask import Blueprint, render_template
from os import path

from src.models.film import Film
from src.views.main.forms import EmptyForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_bp = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    form = EmptyForm()
    films = Film.query.all()
    films_list = []
    for film in films:
        films_list.append(film)
    if form.validate_on_submit():
        ...
    return render_template('home.html', films=films_list, form=form)


@main_bp.route("/about")
def about():
    return render_template('about.html')