from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"


class registration_form(FlaskForm):
    email = StringField("შეიყვანე ელექტრონული ფოსტა", [DataRequired(), length(min=4), Email()])
    first_name = StringField("შეიყვანე სახელი", [DataRequired()])
    last_name = StringField("შეიყვანე გვარი", [DataRequired()])
    submit = SubmitField("Next")


class registration_form2(FlaskForm):
    address = StringField("შეიყვანე მისამართი", [DataRequired()])
    department = StringField("შეიყვანე დეპარტამენტი", [DataRequired()])
    shift = SelectField("სასურველი მორიგეობის განრიგი:",
                        choices=[
                            (16, "16 საათიანი მორიგეობა"),
                            (24, "24 საათიანი მორიგეობა"),
                            {8, "დღის სამსახური"}
                        ])
    submit = SubmitField("Next")


@app.route('/step1', methods=['GET', 'POST'])
def step1():
    email = None
    first_name = None
    last_name = None

    form = registration_form()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        return redirect(url_for('step2'))

    return render_template("home.html", form=form, email=email, first_name=first_name, last_name=last_name)


@app.route('/step2', methods=['GET', 'POST'])
def step2():
    address = None
    department = None
    shift = None

    form = registration_form2()

    if form.validate_on_submit():
        session['address'] = form.address.data
        session['department'] = form.department.data
        session['shift'] = form.shift.data

        return redirect(url_for('validation'))

    return render_template("step2.html", form=form, address=address, department=department, shift=shift)


@app.route('/validation', methods=['GET', 'POST'])
def validation():
    return render_template('validation.html')


if __name__ == '__main__':
    app.run(debug=True, port="4000")
