from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ArticleForm(FlaskForm):
	title = StringField(label="Article Title", validators=[DataRequired(), length(min=10, max=60)])
	body = TextAreaField(label="Article Body", validators=[DataRequired()])
	preview_img = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])


class SignIn(FlaskForm):
	username = StringField(label="Username", validators=[DataRequired()])
	password = PasswordField(label="Password", validators=[DataRequired()])
	remember = BooleanField(label="Remember me")
