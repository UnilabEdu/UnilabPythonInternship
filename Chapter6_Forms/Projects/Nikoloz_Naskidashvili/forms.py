from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class SignIn(FlaskForm):
	username = StringField(label="Username", validators=[DataRequired()])
	password = PasswordField(label="Password", validators=[DataRequired()])
	remember = BooleanField(label="Remember me")
