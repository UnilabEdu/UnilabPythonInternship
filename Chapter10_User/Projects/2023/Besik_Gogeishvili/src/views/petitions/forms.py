from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField, IntegerField, EmailField, SelectField, DateField
from wtforms.validators import DataRequired, length, Email
from flask_wtf.file import FileField
import email_validator


class AddPetition(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"type": "text",
                                                                       "class": "form-control",
                                                                       "placeholder": "Name",
                                                                       "style": "background-color:#ce5a67; border: 0px;"})
    title = StringField("Title", validators=[DataRequired()], render_kw={"type": "text",
                                                                         "class": "form-control",
                                                                         "placeholder": "Title",
                                                                         "style": "background-color:#ce5a67; border: 0px;"})
    address = StringField("Address", validators=[DataRequired()], render_kw={"type": "text",
                                                                             "class": "form-control",
                                                                             "placeholder": "Address",
                                                                             "style": "background-color:#ce5a67; border: 0px;"})
    description = TextAreaField("Description", validators=[DataRequired(), length(min=50)], render_kw={"type": "text",
                                                                                                       "class": "form-control",
                                                                                                       "placeholder": "Description",
                                                                                                       "style": "background-color:#ce5a67; border: 0px;",
                                                                                                       "rows": "10",
                                                                                                       "cols": "45"})
    short_description = TextAreaField("Short Description", validators=[DataRequired(), length(max=200)],
                                      render_kw={"type": "text",
                                                 "class": "form-control",
                                                 "placeholder": "Short Description",
                                                 "style": "background-color:#ce5a67; border: 0px;",
                                                 "rows": "5", "cols": "45"})

    # img upload
    main_img = FileField("main_image", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;",
                                                  "class": "w-100"})
    left_img1 = FileField("first_left_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;",
                                                       "class": "w-100"})
    left_img2 = FileField("second_left_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;",
                                                        "class": "w-100"})
    right_img1 = FileField("first_right_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;",
                                                         "class": "w-100"})
    right_img2 = FileField("second_right_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;",
                                                          "class": "w-100"})

    # img link
    main_img_l = StringField("Main Image Link", render_kw={"type": "text",
                                                           "class": "form-control",
                                                           "style": "background-color:#ce5a67; border: 0px;",
                                                           "placeholder": "Main Image Link"})
    left_img1_l = StringField("First Image Link", render_kw={"type": "text",
                                                             "class": "form-control",
                                                             "style": "background-color:#ce5a67; border: 0px;",
                                                             "placeholder": "First Image Link"})
    left_img2_l = StringField("Second Image Link", render_kw={"type": "text",
                                                              "class": "form-control",
                                                              "style": "background-color:#ce5a67; border: 0px;",
                                                              "placeholder": "Second Image Link"})
    right_img1_l = StringField("Third Image Link", render_kw={"type": "text",
                                                              "class": "form-control",
                                                              "style": "background-color:#ce5a67; border: 0px;",
                                                              "placeholder": "Third Image Link"})
    right_img2_l = StringField("Fourth Image Link", render_kw={"type": "text",
                                                               "class": "form-control",
                                                               "style": "background-color:#ce5a67; border: 0px;",
                                                               "placeholder": "Fourth Image Link"})

    goal = IntegerField("Short Description", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                                     "placeholder": "Number of Signers",
                                                                                     "style": "background-color:#ce5a67; border: 0px;"})

    submit = SubmitField("პეტიციის შექმნა", render_kw={
        "class": "btn",
        "type": "submit",
        "style": "background-color: #ce5a67; margin: 20px; padding: 20px; margin-bottom: 40px;"
    })


class SignPetition(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                       "placeholder": "Name",
                                                                       "style": "background-color:#ce5a67; border: 0px;"})
    surname = StringField("Surname", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                             "placeholder": "Surname",
                                                                             "style": "background-color:#ce5a67; border: 0px;"})
    email = EmailField("Email", validators=[DataRequired(), Email()], render_kw={"class": "form-control",
                                                                                 "placeholder": "Email",
                                                                                 "style": "background-color:#ce5a67; border: 0px;"})
    personal_id = IntegerField("Personal ID", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                                      "placeholder": "Personal ID",
                                                                                      "style": "background-color:#ce5a67; border: 0px;"})
    sex = SelectField("sex", validators=[DataRequired()],
                      choices=[("other", "აირჩიეთ სქესი"), ("male", "მამრობითი"), ("female", "მდედრობითი"),
                               ("other", "სხვა")],
                      render_kw={"class": "form-control",
                                 "placeholder": "Surname",
                                 "style": "background-color:#ce5a67; border: 0px;"})
    number = IntegerField("Phone Number", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                                  "placeholder": "Phone Number",
                                                                                  "style": "background-color:#ce5a67; border: 0px;"})
    city = SelectField("City", validators=[DataRequired()],
                       choices=[("tbilisi", "თბილისი"), ("batumi", "ბათუმი"), ("kutaisi", "ქუთაისი"),
                                ("rustavi", "რუსთავი"), ("gori", "გორი"), ("poti", "ფოთი")],
                       render_kw={"class": "form-control",
                                  "placeholder": "City",
                                  "style": "background-color:#ce5a67; border: 0px;"})
    date = DateField("Birth Date", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                           "placeholder": "Birth Date",
                                                                           "style": "background-color:#ce5a67; border: 0px;"})
    submit = SubmitField("ხელის მოწერა", render_kw={
        "class": "btn",
        "type": "submit",
        "style": "background-color: #ce5a67; margin: 20px; padding: 18px; margin-bottom: 40px;"
    })
