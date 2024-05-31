from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits

from src.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="Password must be at least 8 characters long")])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(),
                                                                   equal_to("password", message="Passwords do not match")])
    submit = SubmitField('Register')

    def validate_email(self, field):
        existing_user = User.query.filter_by(email=field.data).first()
        if existing_user:
            raise ValidationError("This email is already in use")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        for character in field.data:
            if character in ascii_uppercase:
                contains_uppercase = True

            if character in ascii_lowercase:
                contains_lowercase = True

            if character in digits:
                contains_digits = True

        if not contains_uppercase:
            raise ValidationError("Password must contain uppercase letters")
        elif not contains_lowercase:
            raise ValidationError("Password must contain lowercase letters")
        elif not contains_digits:
            raise ValidationError("Password must contain numbers")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')