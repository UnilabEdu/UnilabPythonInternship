from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class AddPost(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(10, 30)])
    post = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Add Post")
