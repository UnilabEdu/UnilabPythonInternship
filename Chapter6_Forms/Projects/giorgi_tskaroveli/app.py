from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"

class registration_form(FlaskForm):
    email = StringField("შეიყვანე ელექტრონული ფოსტა", [DataRequired(), length(min=4), Email()])
    first_name = StringField("შეიყვანე სახელი", [DataRequired()])
    last_name = StringField("შეიყვანე გვარი", [DataRequired()])
    submit = SubmitField("Next")


@app.route('/', methods=['GET', 'POST'])
def home():
    email = None
    first_name = None
    last_name = None

    form = registration_form()

    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        form.email.data = ''
        form.first_name.data = ''
        form.last_name.data = ''

    return render_template("home.html", form=form, email=email, first_name=first_name, last_name=last_name)


if __name__ == '__main__':
    app.run(debug=True)