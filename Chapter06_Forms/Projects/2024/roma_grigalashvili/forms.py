from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, length, equal_to

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="Password must be at least 8 characters long")])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(),
                                                                   equal_to("password", message="Passwords do not match")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Register')
