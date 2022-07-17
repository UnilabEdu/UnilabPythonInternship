from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, BooleanField, SubmitField

class AddForm(FlaskForm):

    name = StringField(label="Enter the name")
    is_active = BooleanField("Is active")
    coach_id = IntegerField("Coach iD")

    submit = SubmitField()


class DeleteForm(FlaskForm):
    name = StringField()

    submit = SubmitField()