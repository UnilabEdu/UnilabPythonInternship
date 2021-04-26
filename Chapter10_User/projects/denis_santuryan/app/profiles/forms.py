from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, RadioField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, length, EqualTo, Email
from app.models import UserModel


class SignInForm(FlaskForm):
    """
    form used for signing in with username or email and password
    can check remember_me to stay logged in
    """
    identifier = StringField('მომხმარებლის სახელი ან ელფოსტა',
                             validators=[
                                 DataRequired(message="მეილის ან იუზერნეიმის შეყვანა აუცილებელია"),
                                 length(min=4, max=100, message="არასწორადაა შეყვანილი"),
                             ])
    login_password = PasswordField('პაროლი',
                                   validators=[
                                       DataRequired(),
                                       length(min=6, max=18),
                                   ])
    remember_me = BooleanField('დამიმახსოვრე')
    submit_login = SubmitField('შესვლა')


class RegisterForm(FlaskForm):
    """
    form used for signing up or updating user data when signed in
    """
    username = StringField('მომხმარებლის სახელი',
                           validators=[
                               DataRequired(message="უნიკალური იუზერნეიმი აუცილებელია"),
                               length(min=6, max=16)
                           ])
    name_first = StringField('სახელი',
                             validators=[
                                 DataRequired(message="სახელის შეყვანა აუცილებელია")
                             ])
    name_last = StringField('გვარი',
                            validators=[
                                DataRequired(message="გვარის შეყვანა აუცილებელია")
                            ])
    email = StringField('ელექტრონული ფოსტა',
                        validators=[
                            DataRequired(message="მეილის შეყვანა აუცილებელია"),
                            length(min=8, max=64, message="არასწორადაა შეყვანილი"),
                            Email(message="არაა შეყვანილი მეილი")
                        ])
    phone = StringField('მობილურის ნომერი',
                        validators=[DataRequired(message="ნომრის შეყვანა აუცილებელია"),
                                    length(min=9, max=20, message="არასწორადაა შეყვანილი")
                                    ])
    dob = StringField('დაბადების თარიღი: ',
                      validators=[
                          DataRequired(message="დაბადების თარიღის შეყვანა აუცილებელია")
                      ])
    sex = RadioField('სქესი: ',
                     choices=[
                         ('Female', 'მდედრობითი'),
                         ('Male', 'მამრობითი'),
                         ('Non-Binary', 'სხვა')
                     ])
    picture = FileField('სურათი (არაა აუცილებელი): ')
    password = PasswordField('ახალი პაროლი',
                             validators=[
                                 EqualTo("conf_pass", message="პაროლები არ ემთხვევა"),
                                 DataRequired(message="პაროლის შეყვანა აუცილებელია"),
                                 length(min=8, max=18, message="პაროლი უნდა შედგებოდეს 8-18 სიმბოლოსგან")
                             ])
    conf_pass = PasswordField('გაიმეორეთ პაროლი')
    submit_register = SubmitField('რეგისტრაცია')
    submit_update = SubmitField('განახლება')

    #  may need to put outside RegisterForm, should delete from routes.py auth()
    def check_already_used(self, username, email):
        temp_username = self.username.data
        temp_email = self.email.data

        if UserModel.find_by_username(temp_username):
            raise ValidationError("მომხმარებლის სახელი დაკავებულია")

        elif UserModel.find_by_email(temp_email):
            raise ValidationError("ელექტრონული ფოსტა დაკავებულია")
