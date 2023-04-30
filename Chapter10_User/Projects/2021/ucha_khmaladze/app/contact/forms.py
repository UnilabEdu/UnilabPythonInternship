from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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