from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegisterForm(FlaskForm):

    email = StringField("Enter your E-Mail",validators=[DataRequired(),Email()])
    password = PasswordField("Enter your password",validators=[DataRequired(),
                                                               length(min=6),
                                                               EqualTo('confirmpassword', message='Passwords must match')])
    confirmpassword = PasswordField("Confirm your password")
    submit = SubmitField("Register")