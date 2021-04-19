from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, IntegerField


class ChoiceForm(FlaskForm):
    choice = RadioField('Are you a student or a tutor?',
                        choices=[
                            ('student', 'Registration for students'),
                            ('tutor', 'Registration for tutors'),
                        ])
    submit = SubmitField('Continue')


class DeleteForm(FlaskForm):
    choice = RadioField('Which one do you want to delete:',
                        choices=[
                            ('student', 'Student'),
                            ('tutor', 'Tutor'),
                        ])
    id = IntegerField('Enter ID')
    submit = SubmitField('Submit')
