import re
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    publication_year = StringField("Publication Year", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    publisher = StringField("Publisher", validators=[DataRequired()])
    submit = SubmitField("Add book")

    def validate_publication_year(self, field):
        publication_year_compiler = re.compile("\s*[1-9]\d{0,3}\s*")
        if not publication_year_compiler.search(field.data):
            raise ValidationError("Invalid publication year date entered.")
