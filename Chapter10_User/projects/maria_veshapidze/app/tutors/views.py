from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user
from app.models import Tutor
from app.tutors.forms import EmailFormTutor, LoginFormTutor
from app.pages_list import nav_bar_pages_list


tutors_blueprint = Blueprint('tutors',
                             __name__,
                             template_folder='templates/tutors'
                             )


@tutors_blueprint.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    form = EmailFormTutor()

    if form.validate_on_submit():
        tutor = Tutor(username=form.username.data,
                      email=form.email.data,
                      password=form.password.data,
                      subject=form.subject.data)

        tutor.add_tutor()

        flash(f"{tutor.username}, You are successfully registered, please log in!")
        return redirect(url_for('tutors.tutor_login'))

    return render_template("register_tutor.html", form=form)


@tutors_blueprint.route('/tutor_login', methods=['GET', 'POST'])
def tutor_login():
    form = LoginFormTutor()
    if form.validate_on_submit():
        user = Tutor.find_by_email(form.email.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("User is successfully logged in!")

            next = request.args.get('next')

            if next is None:
                next = url_for('home')

            return redirect(next)

    return render_template('tutor_login.html', form=form, pages=nav_bar_pages_list)
