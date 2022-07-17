from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[DataRequired])
    password = StringField(label="Password", validators=[L])