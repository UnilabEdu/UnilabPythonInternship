from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile = Blueprint('profile', __name__, template_folder='templates')


@profile.route('/profile')
@login_required
def profile_page():
    favourite_movies = current_user.favourite_movies
    return render_template('profile/profile.html', favourite_movies=favourite_movies)