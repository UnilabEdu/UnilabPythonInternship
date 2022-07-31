from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class Signup(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(4, 20)])
    email = EmailField(validators=[DataRequired(), Email(), Length(10, 30)])
    password = PasswordField(validators=[DataRequired(), Length(8, 30),
                                         EqualTo('conf_pass', message='Passwords must mutch')]
                             )
    conf_pass = PasswordField()
    terms_agree = BooleanField()
    submit = SubmitField('Sign up')

class Login(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(4, 20)])
    password = PasswordField(validators=[DataRequired(), Length(8, 30)])
    remember = BooleanField()
    submit = SubmitField('Log in')