from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField


class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[DataRequired(), Length(min=4, max=8)])
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password")
    confirm_password = PasswordField(label="Confirm Password", validators=[EqualTo('password', message="Passwords don't match")])
    experience = RadioField(choices=[("beginner", "Beginner"), ("some experience", "Some Experience"), ("veteran", "Veteran")])
    account_type = SelectField(choices=[("user", "User"), ("creator", "Creator"), ("venue", "Venue")])
    file_upload = FileField(label="Upload File")
    submit = SubmitField()
