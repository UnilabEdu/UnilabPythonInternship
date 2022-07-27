from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField,PasswordField


class RegisterTable(FlaskForm):
    name = StringField(label="User Name:")
    email = StringField(label="Email:")
    password = PasswordField(label="Password:")
    confirm_password = PasswordField(label="Confirm Password:")
    new_password = PasswordField(label="New Password:")
    submit = SubmitField()