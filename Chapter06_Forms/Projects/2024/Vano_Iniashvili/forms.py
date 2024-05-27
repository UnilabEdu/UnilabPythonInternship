from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class Signin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 64)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField("Sign in")