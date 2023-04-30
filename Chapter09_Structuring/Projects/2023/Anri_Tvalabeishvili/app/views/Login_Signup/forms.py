from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email, length, equal_to


class SignupForm(FlaskForm):
    name_and_surname = StringField(validators=[DataRequired()])
    mobile_number = IntegerField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired("password is required"), length(message="password length not satisfied", min=6, max=16)])
    confirm_password = PasswordField(validators=[DataRequired("confirm password required"),
                                                 equal_to("password", message="Password do not match")])
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()


class Logout(FlaskForm):
    submit = SubmitField()