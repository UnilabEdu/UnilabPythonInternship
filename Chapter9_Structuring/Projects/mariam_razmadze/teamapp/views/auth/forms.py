from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from teamapp.models.user import User
from flask import request
from werkzeug.security import check_password_hash



class RegisterForm(FlaskForm):
    name=StringField(validators=[InputRequired(), Length(min=3, max=50)])
    password=PasswordField(validators=[InputRequired(), Length(min=3, max=50)])
    submit=SubmitField("Register")

    def validate_name(self, name):
        name=request.form['name']
        existing_name=User.query.filter_by(name=name).first()
        if existing_name:
            raise ValidationError("Username already exists. Please choose something else❕")


class LoginForm(FlaskForm):
    name=StringField(validators=[InputRequired(), Length(min=3, max=50)] )
    password=PasswordField(validators=[InputRequired(), Length(min=3, max=50)])
    submit=SubmitField("Login")

    def validate_password(self, password):
        password=request.form['password']
        name=request.form['name']
        user=User.query.filter_by(name=name).first()
        if not user:
            raise ValidationError("Your password is incorrect or this account doesn't exist ❕")
        if not check_password_hash(user.password, password):
                raise ValidationError("Your password is incorrect or this account doesn't exist ❕")