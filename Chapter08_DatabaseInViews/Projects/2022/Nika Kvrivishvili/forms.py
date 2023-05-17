from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


# SelectField_ში ჩაისვას პროგრამის ID
# for-ით უნდა შეიქმნას tuple-ები და ჩაემატოს სიაში, რომელიც გადაეცემა choices-ს


class AddForm(FlaskForm):

    name = StringField('Name: ', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    program_id = SelectField('რომელ პროგრამაზე გსურთ მოხვედრა: ', choices=[('value', 'label')])
    rules = BooleanField('ვეთანხმები წესებს')
    submit = SubmitField('add')


class DelForm(FlaskForm):
    id = IntegerField('ID of Student to Remove:', [DataRequired()])
    delete = SubmitField('remove')


class AddFormAdmin(FlaskForm):
    program = StringField('Program Name: ', [DataRequired()], )
    submit = SubmitField('add')
