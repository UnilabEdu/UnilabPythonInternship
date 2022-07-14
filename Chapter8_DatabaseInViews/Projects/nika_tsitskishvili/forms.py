from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Length
class FilterT(FlaskForm):
    table_name = StringField(label="Choose Table Name:", validators=[Length(min=4, max=20)])
    submit = SubmitField()
class FilterTable(FlaskForm):
    name = StringField(label="Object Name:")
    id = StringField(label="Author's id:") #Novels foreign key
    new_name = StringField(label="New Object Name:")
    new_id = StringField(label="New Author's id:")
    submit = SubmitField()
