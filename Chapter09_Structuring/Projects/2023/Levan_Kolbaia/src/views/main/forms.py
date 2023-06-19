from flask_wtf import FlaskForm
from wtforms.fields import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    goal = RadioField("Goal", choices=["Gain Weight", "Lose Weight"], validators=[DataRequired("Must enter goal")])
    username = StringField("Username", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Submit")