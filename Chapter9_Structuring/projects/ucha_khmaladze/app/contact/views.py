from flask import Blueprint, redirect, render_template, url_for, flash
from app.models import UserInfo
from app.contact.forms import FormName

contact_blueprint = Blueprint('contact',
                              __name__,
                              template_folder='templates')

@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():

    form = FormName()
    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        item = UserInfo(name, lastname, email)
        if UserInfo.read(email):
            pass
        else:
            item.add()

        flash(f"Thank you {name} {lastname} you have successfully sent us a message, we will reach you back on {email}")

        return redirect(url_for("contact.contact"))

    return render_template("contact_us.html", form=form)