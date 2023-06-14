from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
from string import digits

from market.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired("Enter Name")])
    email = EmailField("Email", validators=[DataRequired("Enter Email")])
    password = PasswordField("Password", validators=[DataRequired("Enter Password"), length(min=8, max=64,
                                                                                            message="Password must be min 8 and max 64 symbol")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired("Confirm Password"),
                                                                     equal_to("password",
                                                                              message="passwords does't mutch")])
    submit = SubmitField("Register")

    def validate_username(self, field):
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user:
            raise ValidationError("User already exists")

    def validate_email(self, field):
        existing_email = User.query.filter_by(email=field.data).first()
        if existing_email:
            raise ValidationError("Email already exists")


    def validate_password(self, field):
        contains_digits = False
        for char in field.data:
            if char in digits:
                contains_digits = True

        if not contains_digits:
            raise ValidationError("Password must contains digits")


class LoginForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired("Enter Name")])
    password = PasswordField("Password", validators=[DataRequired("Enter Password"), length(min=8, max=64,
                                                                message="Password must be min 8 and max 64 symbol")])
    submit = SubmitField("Login")