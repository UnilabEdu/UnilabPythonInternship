from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class AddPost(FlaskForm):
    title = StringField(validators=[DataRequired()])
    post = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Add Post')

class DeletePost(FlaskForm):
    post_id = StringField(validators=[DataRequired()])
    submit = SubmitField('Delete Post')
