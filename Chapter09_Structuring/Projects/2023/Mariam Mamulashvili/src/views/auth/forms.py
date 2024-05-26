from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    company = StringField('Company')
    message = StringField("What's your quiry?", validators=[DataRequired()])
    submit = SubmitField('Submit')