from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    login = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Log In')


class SignupForm(FlaskForm):

    email = StringField('Email',[DataRequired(), Email()])
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password',[DataRequired()])
    confirm_password = PasswordField('Repeat password', [DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')