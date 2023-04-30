from wtforms import StringField, SubmitField, validators, EmailField, FileField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed


class UserForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25),DataRequired()], render_kw={"autocomplete": "off"})
    email = EmailField('Email Address', [DataRequired()])
    first_name = StringField('First Name', [validators.Length(min=3, max=120),DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=3, max=120),DataRequired()])
    course = StringField('Course', [validators.Length(min=3, max=120),DataRequired()])
    university = StringField('University', [validators.Length(min=3, max=120),DataRequired()])
    file = FileField('image', [FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])

