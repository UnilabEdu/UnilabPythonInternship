from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from source.user.models import User


class BaseForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=4, max=24)])
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password")
    confirm_password = PasswordField(label="Confirm Password", validators=[EqualTo('password', message="Passwords don't match")])
    experience = RadioField(choices=[("beginner", "Beginner"), ("some experience", "Some Experience"), ("veteran", "Veteran")])
    account_type = SelectField(choices=[(1, "User"), (2, "Creator"), (3, "Venue")])
    submit = SubmitField()

    def validate_email_from_db(self):
        temp_email = self.email.data
        if User.find_by_email(temp_email):
            raise ValidationError("Email already exists")


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class GetForm(FlaskForm):
    id = IntegerField('User ID')
    submit = SubmitField("Submit")
