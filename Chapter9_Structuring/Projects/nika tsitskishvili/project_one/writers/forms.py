from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Length

class FilterTable(FlaskForm):
    name = StringField(label="Object Name:")
    new_name = StringField(label="New Object Name:")
    submit = SubmitField()
