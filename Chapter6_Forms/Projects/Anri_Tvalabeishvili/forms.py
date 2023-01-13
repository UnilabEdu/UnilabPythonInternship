from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired(),Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=5)])
    submit = SubmitField()


class Auctorisation(FlaskForm):
    email = EmailField(validators=[DataRequired(),Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=5)])
    submit_aut = SubmitField()