from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, RadioField, TextAreaField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField(label="Username: ", validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField(label="Enter your password: ", validators=[DataRequired()])
    confirm_pass = PasswordField(label="Confirm password", validators=[EqualTo('password', message="The passwords are not the same")])
    email = EmailField(label="Enter your email")
    gender = RadioField(label="Gender", choices=[("male", "Male"), ("female", "Female")])

    file = FileField(label="Upload a photo", validators=[FileAllowed(['jpg', 'png'], 'Upload images only')])
    date = DateField(label="Date of birth")
    approval = BooleanField(label="Agree?", validators=[DataRequired()])
    submit = SubmitField()


