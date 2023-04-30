from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from app.auth.models import User


class SignInForm(FlaskForm):
	username = StringField(label="Username", validators=[DataRequired()])
	password = PasswordField(label="Password", validators=[DataRequired()])
	remember = BooleanField(label="Remember me")


class SignUpForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password1 = PasswordField('Password',
		validators=[DataRequired(), EqualTo('password2', message='Passwords Must Match!')]
	)
	password2 = PasswordField('Confirm password', validators=[DataRequired()])
