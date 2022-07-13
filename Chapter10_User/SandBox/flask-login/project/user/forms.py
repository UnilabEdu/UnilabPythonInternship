from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo
from wtforms import ValidationError

from project.user.models import User


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('pass_confirm')])
    pass_confirm = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("register")

    def validate_email_from_db(self):
        temp_email = self.email.data
        if User.find_by_email(temp_email):
            raise ValidationError("Email already exists")

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("register")