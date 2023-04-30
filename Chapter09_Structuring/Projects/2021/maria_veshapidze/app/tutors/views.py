from flask import Blueprint, redirect, url_for, render_template, flash
from app.models import Tutor
from app.tutors.forms import EmailFormTutor


tutors_blueprint = Blueprint('tutors',
                             __name__,
                             template_folder='templates/tutors'
                             )


@tutors_blueprint.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    email = None
    password = None

    form = EmailFormTutor()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        subject = form.subject.data

        item = Tutor(name, email, password, subject)
        item.add_tutor()

        flash(f"{name}, You were successfully registered!")
        return redirect(url_for('tutors.register_tutor'))

    return render_template("register_tutor.html", form=form, email=email, password=password)
