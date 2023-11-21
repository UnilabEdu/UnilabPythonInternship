from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, length, equal_to
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
                                                                        "rows":"10", "cols":"45"})
    short_description = StringField("Short Description", validators=[DataRequired(), length(max=200)], render_kw={"type": "text", 
                                                                       "class": "form-control", 
                                                                       "placeholder": "Short Description",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})

    # img upload
    main_img = FileField("main_image", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;", 
                                                  "class":"w-100"})
    left_img1 = FileField("first_left_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;", 
                                                  "class":"w-100"})
    left_img2 = FileField("second_left_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;", 
                                                  "class":"w-100"})
    right_img1 = FileField("first_right_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;", 
                                                  "class":"w-100"})
    right_img2 = FileField("second_right_img", render_kw={"style": "background-color:#ce5a67; border-radius: 5px;", 
                                                  "class":"w-100"})


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


    submit = SubmitField("პეტიციის შექმნა", render_kw={
        "class":"btn", 
        "type":"submit", 
        "style": "background-color: #ce5a67; margin: 20px; padding: 20px; margin-bottom: 40px;"
    })


class Register(FlaskForm):
    username = StringField("username", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Username",
                                                                       "cols": "45",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    name = StringField("name", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Name",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    last_name = StringField("lastname", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Last Name",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    email = EmailField("email", validators=[DataRequired(), Email()], render_kw={"class": "form-control", 
                                                                       "placeholder": "example@mail.com",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    password = PasswordField("password", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Password",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    
    repeat_password = PasswordField("repeat_password", validators=[DataRequired(), equal_to("password", message="პაროლები არ ემთხვევა")] , 
                                                                    render_kw={"class": "form-control",
                                                                       "placeholder": "Repeat Password",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})  

    submit = SubmitField("რეგისტრაცია", render_kw={
        "class":"btn", 
        "style": "background-color: #ce5a67; margin: 20px; padding: 15px; margin-bottom: 40px;"
    })



class Login(FlaskForm):
    username = StringField("username", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Username",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    
    password = PasswordField("password", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Password",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    
    # დამახსოვრება
    
    submit = SubmitField("შესვლა", render_kw={
        "class":"btn", 
        "style": "background-color: #ce5a67; margin: 20px; padding: 15px; margin-bottom: 40px;"
    })
