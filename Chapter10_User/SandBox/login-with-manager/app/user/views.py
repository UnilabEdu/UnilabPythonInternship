from flask import Blueprint, redirect, url_for

from flask_user import current_user

members_blueprint = Blueprint('member',
                              __name__,
                              template_folder='template')

@members_blueprint.route('/logout')
def logout():
    logout()