from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField
from wtforms.validators import InputRequired
from teamapp.models.user import User
from flask import request
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy import or_
from teamapp.extensions import db


class AnswerForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])


def user_query():
    return User.query.filter(db.or_(User.senior==True, User.junior==True))


class AskForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])
    options=QuerySelectField(query_factory=user_query, allow_blank=False, get_label='name')


class RadioForm(FlaskForm):
    radio=RadioField('Radios', choices=[('senior', 'Senior'), ('junior', 'Junior'), ('intern', 'Intern')])