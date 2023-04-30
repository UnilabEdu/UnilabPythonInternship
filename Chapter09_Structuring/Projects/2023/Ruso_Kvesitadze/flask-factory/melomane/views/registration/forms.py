from wtforms.fields import StringField, PasswordField, EmailField, RadioField, BooleanField, SelectField, TextAreaField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length, equal_to, Email

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired("username is required")])
    email = EmailField(validators=[DataRequired(), Email()])

    password = PasswordField(validators=[DataRequired("password is required"),
                                         length(message="password length not satisfied", min=8, max=16)])
    confirm_password = PasswordField(validators=[DataRequired("confirm password required"),
                                                 equal_to("password", message="Password do not match")])

    submit = SubmitField()
