from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user


from app.models import User
# style="width: 20%; margin-left: 40%;"

# make LoginForm autocomplete off
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)], render_kw={'class': 'form-control','autocomplete':'off'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)],render_kw={'class': 'form-control'})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={'class': 'form-control'})
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class UpdateAccountForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={'class': 'form-control'})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)], render_kw={'class': 'form-control'})
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class DeleteAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={'class': 'form-control'})
    submit = SubmitField('Delete')

