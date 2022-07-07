from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import ValidationError

class RegistrtionForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    selfid = StringField(null=True, unique=True, max_length=11, validators=[min(11, message='Card ID Length has to be contain 11 integer : ***********'), only_int],)

    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

    def only_int(self): 
        if self.isdigit()==False:
            raise ValidationError('ERROR: ID contains characters, it only contains integers:')  