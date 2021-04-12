from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField("სტუდენტის სახელი")
    submit = SubmitField("დამატება")


class DelForm(FlaskForm):
    name = IntegerField("სტუდენტის ID")
    submit = SubmitField("წაშლა")
