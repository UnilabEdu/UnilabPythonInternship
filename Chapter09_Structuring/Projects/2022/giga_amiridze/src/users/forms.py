from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Signup(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(4, 20)])
    email = EmailField(validators=[DataRequired(), Email(), Length(15, 30)])
    password = PasswordField(validators=[DataRequired(), Length(8, 20),
                                         EqualTo('conf_pass', message='Passwords must mutch')]
                             )
    conf_pass = PasswordField()
    terms_agree = BooleanField()
    submit = SubmitField("Register")
