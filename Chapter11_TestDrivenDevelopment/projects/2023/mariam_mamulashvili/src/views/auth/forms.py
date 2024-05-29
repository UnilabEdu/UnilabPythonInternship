from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email
from flask_wtf.file import FileField
from string import ascii_uppercase, ascii_lowercase, digits
from email_validator import validate_email, EmailNotValidError

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])    
    phone = StringField('Phone Number', validators=[DataRequired()])
    company = StringField('Company')
    message = StringField("What's your quiry?", validators=[DataRequired()])
    submit = SubmitField('Submit')



class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    