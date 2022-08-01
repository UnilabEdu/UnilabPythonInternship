from flask import Blueprint, render_template

profiles_blueprint = Blueprint('profile',
                               __name__,
                               template_folder='templates/profiles'
                               )

@profiles_blueprint.route('/profile')
def profile():
    return render_template('profile.html')