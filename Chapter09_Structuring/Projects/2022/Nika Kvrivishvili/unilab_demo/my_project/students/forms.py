from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Name: ', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    program_id = SelectField('რომელ პროგრამაზე გსურთ მოხვედრა: ', choices=[('value', 'label')])
    rules = BooleanField('ვეთანხმები წესებს')
    submit = SubmitField('add')


class DelForm(FlaskForm):
    id = IntegerField('ID of Student to Remove:', [DataRequired()])
    delete = SubmitField('remove')
