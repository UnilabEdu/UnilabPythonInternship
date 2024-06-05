from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, DateField, FileField
from wtforms.validators import DataRequired, Email, Length


class Signin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 64)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField("Sign in")


class UploadFilm(FlaskForm):
    title = StringField("Film Name", validators=[DataRequired()])
    director = StringField("Director")
    genre = StringField("Genre")
    release_date = DateField("Release Date")
    cover = FileField("Film Cover")
    submit = SubmitField("Upload")