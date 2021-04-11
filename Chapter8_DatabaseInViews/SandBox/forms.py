from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField, IntegerField


class AddForm(FlaskForm):
    name = StringField('name')
    param1 = TextAreaField('param1')
    param2 = RadioField('param2',
                        choices=[(True, 'True')])
    submit = SubmitField('Submit')


class DeleteForm(FlaskForm):
    id = IntegerField('ID of item')
    submit = SubmitField('Submit')
