from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

class EmptyForm(FlaskForm):
    button = SubmitField('Button')
