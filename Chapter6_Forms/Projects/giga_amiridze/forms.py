from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, DateField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForms(FlaskForm):
    first_name = StringField(validators=[DataRequired(message="Please input your first name")])
    last_name = StringField(validators=[DataRequired(message="Please input your last name")])
    email = EmailField(validators=[Email(), DataRequired(message="Please input your email")])
    password = PasswordField(validators=[DataRequired(), Length(8, 20), EqualTo("password", message="Passwords do not match")])
    confirm_pass = PasswordField(validators=[DataRequired()])
    birth_date = DateField(validators=[DataRequired()])
    gender = RadioField(choices=[("male", "Male"), ("female", "Female")], validators=[DataRequired()])
    submit = SubmitField("Submit")