from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[Length(min=4, max=20)])
    password = PasswordField(label="Password", validators=[Length(min=8, max=20)])
    email = EmailField(label="e-mail", validators=[Email()])
    confirmpassword = PasswordField(label="Confirm Password",validators=[EqualTo("password", message="Passwords do not match!")])
    gender = RadioField(choices=[("male","Male"),("female","Female")])
    # textarea =TextAreaField()
    submit = SubmitField()