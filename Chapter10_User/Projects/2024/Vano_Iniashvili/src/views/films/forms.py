from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, DateField, FileField
from wtforms.validators import DataRequired


class UploadFilm(FlaskForm):
    title = StringField("Film Name", validators=[DataRequired()])
    director = StringField("Director")
    genre = StringField("Genre")
    release_date = DateField("Release Date")
    cover = FileField("Film Cover")
    submit = SubmitField("Upload")