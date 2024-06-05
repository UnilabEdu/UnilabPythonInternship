from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, RadioField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired,length,equal_to,ValidationError
from string import punctuation


class RegisterForm(FlaskForm):

    username = StringField('შეიყვანეთ username',validators=[DataRequired(),length(min=8,max=12)])
    password = PasswordField("შეიყვანეთ პაროლი",validators=[DataRequired(),length(min=8,max=12)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი",validators=[DataRequired(),equal_to("password")])
    age =  DateField(validators=[DataRequired()])
    gender = RadioField( choices=["Male","Female"],validators=[DataRequired()])
    nationality = SelectField(choices=["Georgia","Usa","UK"],validators=[DataRequired()])
    submit = SubmitField()
    


    def validate_password(self,field):
        contains_symbol = False
        

        for char in field.data:
            if char in punctuation :
                contains_symbol = True

        if not contains_symbol:
            raise ValidationError("username must contain symbol")
    def validate_username(self,field):
        contains_symbol = False
        for char in field.data:
             
             if char in punctuation :
                contains_symbol = True

        if not contains_symbol:
            raise ValidationError("password must contain symbol")
        