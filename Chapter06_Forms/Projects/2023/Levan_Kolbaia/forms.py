from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
#from string import ascii_uppercase, ascii_lowercase, digits, punctuation


class RegisterForm(FlaskForm):
    goal = RadioField("Goal", choices=["Gain Weight", "Lose Weight"], validators=[DataRequired("Must enter goal")])
    username = StringField("Username", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Submit")