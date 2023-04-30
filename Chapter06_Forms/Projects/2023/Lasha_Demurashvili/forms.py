from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):

    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField()

