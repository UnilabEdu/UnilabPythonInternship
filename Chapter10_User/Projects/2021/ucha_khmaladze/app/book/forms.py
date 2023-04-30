from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, length

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

    select_adult = SelectField('Number of adults', choices=["1","2","3","4","5"])
    select_child = SelectField('Number of children (under 6 years)', choices=['1',"2","3","4","5"])
    submit = SubmitField('Submit reservation')