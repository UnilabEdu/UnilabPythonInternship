from flask import Blueprint, render_template
from src.resources.pages import nav_bar_pages

public_blueprint = Blueprint('public',
                             __name__,
                             template_folder='templates/public'
                             )

@public_blueprint.route('/home')
def home():
    return render_template('home.html', pages=nav_bar_pages)

@public_blueprint.route('/profile')
def profile():
    return render_template('profile.html', pages=nav_bar_pages)
