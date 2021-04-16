from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, length, InputRequired, Email
from wtforms.widgets import TextArea


class FormName(FlaskForm):
    name = StringField('First Name',
                       validators=[
                           DataRequired(),
                           length(min=2, max=35)
                       ],
                       render_kw={"placeholder":"E.g John"}
                       )
    lastname = StringField('Last Name',
                           validators=[
                               DataRequired(),
                               length(min=2, max=35)
                           ],
                           render_kw={"placeholder": "E.g Smith"}
                           )
    email = StringField('Enter your E-mail',
                        validators=[
                            InputRequired(),
                            length(max=35),
                            Email(message="Wrong format!")
                        ],
                        render_kw={"pLaceholder": "example@example.com"}
                        )
    message = StringField('Leave your message here!', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Submit')

class FormBook(FlaskForm):
    name = StringField('First Name',
                       validators=[
                           DataRequired(),
                           length(min=2, max=35)
                       ],
                       render_kw={"placeholder":"E.g John"}
                       )
    lastname = StringField('Last Name',
                           validators=[
                               DataRequired(),
                               length(min=2, max=35)
                           ],
                           render_kw={"placeholder": "E.g Smith"}
                           )
    date_from = DateField('From')
    date_to = DateField('To')
    select_adult = SelectField('Number of adults', choices=[("1"),("2"),("3"),("4"),("5")])
    select_child = SelectField('Number of children (under 6 years)', choices=[("1"), ("2"), ("3"), ("4"), ("5")])
    submit = SubmitField('Submit reservation')