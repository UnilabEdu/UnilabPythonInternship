from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField


class AddForm(FlaskForm):
    name = StringField("Players Name")
    surname = StringField("Players Surname")
    team = RadioField ("Teams", choices=[
                            ("Golden State"),
                            ("Lakers"),
                            ("Milwauke"),
                            ("Boston"),
    ])
    submit = SubmitField("Add")
    id = IntegerField("Players Id")




class DeleteForm(FlaskForm):
    id = IntegerField("Players Id")
    submit = SubmitField("Delete")
