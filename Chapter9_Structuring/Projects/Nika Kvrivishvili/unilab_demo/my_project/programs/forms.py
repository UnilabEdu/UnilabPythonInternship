from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProgramForm(FlaskForm):
    program = StringField('Program Name: ', [DataRequired()], )
    submit = SubmitField('add')
