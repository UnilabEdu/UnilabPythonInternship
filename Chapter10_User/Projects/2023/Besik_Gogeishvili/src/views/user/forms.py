from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, equal_to, length


class EditUser(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Name",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    surname = StringField("surname", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Last Name",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    password = PasswordField("password", validators=[DataRequired()], render_kw={"class": "form-control", 
                                                                       "placeholder": "Password",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})
    
    repeat_password = PasswordField("repeat_password", validators=[DataRequired(), equal_to("password", message="პაროლები არ ემთხვევა")] , 
                                                                    render_kw={"class": "form-control",
                                                                       "placeholder": "Repeat Password",
                                                                        "style": "background-color:#ce5a67; border: 0px;"})  

    submit = SubmitField("დადასტურება", render_kw={
        "class":"btn", 
        "style": "background-color: #ce5a67; margin: 20px; padding: 15px; margin-bottom: 40px;"
    })


class EditPetition(FlaskForm):
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

    submit = SubmitField("პეტიციის რედაქტირება", render_kw={
        "class":"btn", 
        "type":"submit", 
        "style": "background-color: #ce5a67; margin: 20px; padding: 20px; margin-bottom: 40px;"
    })
