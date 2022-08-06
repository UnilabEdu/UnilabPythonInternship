from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from wtforms import ValidationError
from src.models import User

class Signup(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(4, 20)])
    email = EmailField(validators=[DataRequired(), Email(), Length(10, 30)])
    password = PasswordField(validators=[DataRequired(), Length(8, 30),
                                         EqualTo('conf_pass', message='Passwords must mutch')]
                             )
    conf_pass = PasswordField()
    terms_agree = BooleanField()
    submit = SubmitField('Sign up')

    def validate_email_from_db(self):
        temp_email = self.email.data
        if User.find_by_email(temp_email):
            raise ValidationError("Email already exists")

class Login(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField()
    submit = SubmitField('Log in')