from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField
from wtforms.validators import InputRequired
from teamapp.models.user import User, Role
from flask import request
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy import or_
from teamapp.extensions import db


class AnswerForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])


def user_query():
    return User.query.filter(User.roles.any(db.or_(Role.name=='senior', Role.name=='junior')))


class AskForm(FlaskForm):
    textarea=TextAreaField(validators=[InputRequired()])
    options=QuerySelectField(query_factory=user_query, allow_blank=False, get_label='name')

