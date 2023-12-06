from flask import render_template, url_for, redirect, Blueprint
from src.views.auth.forms import ContactForm 

from uuid import uuid4


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print('Form validated')
        return redirect(url_for('main.home'))
    return render_template('auth/contact.html', is_admin=True, form=form)