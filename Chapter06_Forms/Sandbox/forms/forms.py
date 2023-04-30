from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[Length(min=4, max=8)])
    email = EmailField(label="Enter Email", validators=[Email()])
    password = PasswordField(label="Enter Password")
    confirmpassword = PasswordField(label="Confirm Password",
                                    validators=EqualTo("password", message="Passwords does not match"))
    gender = RadioField(choices=[("firstchoice", 'Male'), ("secondchoice", 'female')])
    textarea = TextAreaField()
    submit = SubmitField
