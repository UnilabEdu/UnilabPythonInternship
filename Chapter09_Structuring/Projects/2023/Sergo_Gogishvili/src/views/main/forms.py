from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, IntegerRangeField
from wtforms.validators import DataRequired, equal_to, length


class RegisterForm(FlaskForm):

    username = StringField("username", validators=[(DataRequired())])
    password = PasswordField("password",validators=[DataRequired(), length(min=5, max=15, message="შეიყვანეთ მინიმუმ 5 და მაქსიმუმ 15 სიმბოლო")])
    gender = RadioField("აირჩიეთ სქესი", choices=["მამრობითი","მდედრობითი"], validators=[(DataRequired())])
    birthday=DateField("დაბადების თარიღი",validators=[(DataRequired())])
    sports = SelectField("აირჩიეთ აქტივობა",choices=["ჩამონათვალი","იოგა","ქროსფითი","პილატესი","ძიუდო","ფიტნესი"], validators=[(DataRequired())])
    submit = SubmitField("რეგისტრაცია")
    repeat_password = PasswordField("repeat password", validators=[DataRequired(),equal_to("password",message="პაროელები არ ემთხვევა")])
    range = IntegerRangeField("შეიყვანეთ წონა",
                              render_kw={"min": 40, "max": 200})

class AboutForm(FlaskForm):
    texstarea = TextAreaField("რა არის თქვენი მიზანი?")
    texstareatwo = TextAreaField("გაქვთ თუ არა საკმარისი მოტივაცია?")
    send = SubmitField("გაგზავნა")