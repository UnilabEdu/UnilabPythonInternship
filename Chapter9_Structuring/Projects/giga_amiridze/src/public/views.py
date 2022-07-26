from flask import Blueprint, render_template

public_blueprint = Blueprint('public',
                             __name__,
                             template_folder='templates/public'
                             )

@public_blueprint.route('/home')
def home():
    return render_template('home.html')

@public_blueprint.route('/profile')
def profile():
    return render_template('profile.html')
