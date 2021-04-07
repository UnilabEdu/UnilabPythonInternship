from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField


class AddForm(FlaskForm):
    name = StringField('name')
    param1 = TextAreaField('param1')
    param2 = RadioField('param2',
                        choices=[(1, 'Yes'),
                                 (0, 'NO')])
    submit = SubmitField('Submit')
