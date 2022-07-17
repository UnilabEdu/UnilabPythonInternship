from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ArticleForm(FlaskForm):
	title = StringField(label="Article Title", validators=[DataRequired(), length(min=10, max=60)])
	body = TextAreaField(label="Article Body", validators=[DataRequired()])
	preview_img = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
