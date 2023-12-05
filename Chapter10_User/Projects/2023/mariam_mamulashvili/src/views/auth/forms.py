from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from flask_wtf.file import FileField
from string import ascii_uppercase, ascii_lowercase, digits


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    company = StringField('Company')
    message = StringField("What's your quiry?", validators=[DataRequired()])
    submit = SubmitField('Submit')



class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    