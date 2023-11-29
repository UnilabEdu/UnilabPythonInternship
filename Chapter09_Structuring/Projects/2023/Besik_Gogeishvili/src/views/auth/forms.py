from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, equal_to
import email_validator


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
    