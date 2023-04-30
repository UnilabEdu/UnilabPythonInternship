from flask import Blueprint, render_template
from app.models.movie import Movie

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home_page():
    all_movies = Movie.read_all()
    return render_template('main/index.html', movies=all_movies)