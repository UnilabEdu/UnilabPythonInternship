from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


public_blueprint = Blueprint('public',
                             __name__,
                             template_folder='../templates')

@public_blueprint.route('/')
@public_blueprint.route('/home')
@login_required
def home_page():

    return render_template('home.html')