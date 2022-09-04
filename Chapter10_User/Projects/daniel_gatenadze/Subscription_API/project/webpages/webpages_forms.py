from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed


class UserProfile(FlaskForm):
    username = StringField(label="Enter Username",
                           validators=[DataRequired(message="Please Enter Correct Username"), Length(min=8, max=64)],
                           render_kw={"placeholder": "username"})
    email = EmailField(label="Enter your email",
                       validators=[Email(check_deliverability=False, message="Please Enter Correct Email")],
                       render_kw={"placeholder": "email"})
    password = PasswordField(label="Enter Password",
                             validators=[DataRequired(message="Please Enter Correct Password"),
                                         Length(min=8, max=64)], render_kw={"placeholder": "Password"})
    confirmpassword = PasswordField(label="Confirm Password",
                                    validators=[EqualTo("password", message="passwords don't match")],
                                    render_kw={"placeholder": "Confirm Password"})
    gender = RadioField(choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    age = IntegerField(label="Age", render_kw={"placeholder": "Age"})
    profile_pic = FileField(label="Upload Avatar", validators=[FileAllowed(['png', 'jgp'])])
    about = TextAreaField(label='About Yourself',validators=[DataRequired()],render_kw={"placeholder": "About"})
    submit = SubmitField()


class CheckoutForm(FlaskForm):
    name_card = StringField(validators=[DataRequired(Length(min=8, max=64))], render_kw={"placeholder": "John Doe"})
    card_num = IntegerField(validators=[DataRequired(Length(min=12, max=16))],render_kw={"placeholder": "1111-2222"
                                                                                                        "-3333-4444"})
    cvv = IntegerField(validators=[DataRequired(Length(min=3, max=6))],render_kw={"placeholder": "123"})
    full_name = StringField(label="John M. Doe",
                            validators=[DataRequired(message="Please Enter Correct Name"), Length(min=5, max=64)],
                            render_kw={"placeholder": "John M. Doe"})
    email = EmailField(label="Enter your email",
                       validators=[Email(check_deliverability=False, message="Please Enter Correct Email")],
                       render_kw={"placeholder": "john@example.com"})
    address = StringField(label='address', validators=[DataRequired(message="Please Enter Correct Name")],
                          render_kw={"placeholder": "Street S. 8th"})
    zip_code = IntegerField(validators=[DataRequired(Length(min=0, max=15))], render_kw={"placeholder": "Zip Code"})
    state = StringField(label='state', render_kw={"placeholder": "State"})
    submit = SubmitField()
