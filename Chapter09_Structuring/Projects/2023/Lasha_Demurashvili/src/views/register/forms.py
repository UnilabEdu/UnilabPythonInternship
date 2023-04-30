from wtforms.fields import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):

    username = StringField(validators=[DataRequired("username is required")])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired("password is required")])

    submit = SubmitField()

