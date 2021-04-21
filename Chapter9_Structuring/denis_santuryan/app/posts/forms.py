from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, TextAreaField


class PostForm(FlaskForm):
    text = TextAreaField('პოსტის ტექსტი')
    media = FileField('ასატვირთი სურათი')
    submit_post = SubmitField('დაპოსტვა')
