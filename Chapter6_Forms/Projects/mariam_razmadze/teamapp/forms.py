from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired, Length, ValidationError
from .models import User
from flask import request
from werkzeug.security import check_password_hash
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy import or_
from .extensions import db




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

class AnswerForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])


def user_query():
    return User.query.filter(db.or_(User.senior==True, User.junior==True))


class AskForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])
    options=QuerySelectField(query_factory=user_query, allow_blank=False, get_label='name')


class RadioForm(FlaskForm):
    radio=RadioField('Radios', choices=[('senior', 'Senior'), ('junior', 'Junior'), ('intern', 'Intern')])




