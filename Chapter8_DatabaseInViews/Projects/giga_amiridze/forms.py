from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class AddForm(FlaskForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    age = IntegerField(validators=[DataRequired()])
    email = EmailField(validators=[Email(), DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    id = IntegerField('ID of item')
    submit = SubmitField('Submit')
