from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, Email


class registration_form(FlaskForm):
    email = StringField("შეიყვანე ელექტრონული ფოსტა", [DataRequired(), length(min=4), Email()])
    first_name = StringField("შეიყვანე სახელი", [DataRequired()])
    last_name = StringField("შეიყვანე გვარი", [DataRequired()])
    submit = SubmitField("Next")


class registration_form2(FlaskForm):
    address = StringField("შეიყვანე მისამართი", [DataRequired()])
    department = StringField("შეიყვანე დეპარტამენტი", [DataRequired()])
    shift = SelectField("სასურველი მორიგეობის განრიგი:",
                        choices=[
                            (16, "16 საათიანი მორიგეობა"),
                            (24, "24 საათიანი მორიგეობა"),
                            {8, "დღის სამსახური"}
                        ])
    submit = SubmitField("Next")


class final_save_to_db(FlaskForm):
    submit = SubmitField("Save")
