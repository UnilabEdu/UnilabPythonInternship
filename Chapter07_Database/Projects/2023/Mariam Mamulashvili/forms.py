from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,  FileAllowed 

class AddMediaForm(FlaskForm):
    product_name = StringField('Video Title')
    description= StringField('Description')
    product_image = FileField('Upload Image/Video')
    product_category = SelectField('Media Category', choices=[('video', 'Video'), ('image', 'Image')])
    page_category = SelectField('Page Category', choices=[('galley', 'Gallery'),
                                                        ('gimbal', 'Gimbal'), 
                                                        ('pyrotechnics', 'Pyrotechnics'),
                                                        ('model_making', 'Model Making'), 
                                                        ('prosthetics', 'Prosthetics'),
                                                        ('atmospherics', 'Atmospherics')], 
                                                        validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    company = StringField('Company')
    message = StringField("What's your quiry?", validators=[DataRequired()])
    submit = SubmitField('Submit')

    