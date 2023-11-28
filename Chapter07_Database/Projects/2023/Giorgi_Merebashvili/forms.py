from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

SPORTS = [
    'Football', 'Basketball', 'Volleyball'
]

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[(DataRequired())])
    age = IntegerField('Age', validators=[(DataRequired())])
    sport = SelectField('Sport', choices=SPORTS , validators=[(DataRequired())])
    submit = SubmitField('Register', validators=[(DataRequired())])

    