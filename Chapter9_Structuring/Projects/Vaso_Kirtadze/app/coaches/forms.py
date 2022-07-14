from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField("Enter the name")
    age = IntegerField("age")
    submit = SubmitField('submit')


class DeleteForm(FlaskForm):
    name = StringField("Enter the name")
    submit = SubmitField('submit')