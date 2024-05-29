from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField


class AddMediaForm(FlaskForm):
    product_name = StringField('Video Title')
    description= StringField('Description')
    product_image = StringField('Image/Video URL')
    product_category = SelectField('Category', choices=[('video', 'Video'), ('image', 'Image')])
    submit = SubmitField('Submit')

    