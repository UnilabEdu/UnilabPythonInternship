from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField, SelectField, TextField
from wtforms.validators import DataRequired, length, Email, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = "SecretKey"


class EmailForm(FlaskForm):
    name = StringField("Enter your name:", [DataRequired(), length(min=2, max=15)])

    email = StringField("Enter your email:",
                        validators=[
                            DataRequired(),
                            length(min=4),
                            Email()
                        ]
                        )

    password = PasswordField("Enter a password:",
                        validators=[
                            DataRequired(),
                            length(min=6),
                            EqualTo("confirm_password", message="Passwords do not match")
                        ]
                        )

    confirm_password = PasswordField("Reenter a password:")

    student = RadioField('Are you a student?',
                         choices=[
                            ('1', 'yes'),
                            ('0', 'no'),
                        ])

    living_place = SelectField(u'Indicate your living place:', choices=[('tb', 'Tbilisi'), ('ba', 'Batumi'), ('tl', 'Telavi'), ('oth', 'Other')])

    feedback = TextField('Enter a comment')

    submit = SubmitField("Submit")


class SimpleForm(FlaskForm):
    submit = SubmitField('Confirm')


nav_bar_pages_list = (
    ("home", "Home",),
    ("about", "About us"),
    ("contact", "Contact Info"),
    ("registration", "Registration")
)


@app.route('/')
@app.route('/<guestname>')
def home(guestname=None):
    return render_template("home_page.html", name=guestname, pages=nav_bar_pages_list)


@app.route('/about_us')
def about():
    return render_template("about_us.html", pages=nav_bar_pages_list)


@app.route('/contact_info')
def contact():
    return render_template("contact_info.html", pages=nav_bar_pages_list)


@app.route('/reg', methods=['GET', 'POST'])
def registration():
    email = None
    password = None

    form = EmailForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        session['student'] = form.student.data
        session['living_place'] = form.living_place.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('confirmation'))

    return render_template("registration.html", pages=nav_bar_pages_list, form=form, email=email, password=password)


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    form = SimpleForm()

    if form.validate_on_submit():
        flash("You are successfully registered!")
        return redirect(url_for('confirmation'))

    return render_template('confirmation_page.html', form=form)


if __name__ == '__main__':
    app.run(port=8086, debug=True)