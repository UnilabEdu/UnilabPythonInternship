from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[(DataRequired())])
    email = EmailField('Email', validators=[(DataRequired())])
    password = PasswordField('Password', validators=[(DataRequired())])
    submit = SubmitField('Register', validators=[(DataRequired())])

    