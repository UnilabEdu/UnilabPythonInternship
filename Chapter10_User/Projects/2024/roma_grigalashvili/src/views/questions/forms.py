from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question_text = StringField('Question', validators=[DataRequired()])
    choice1 = StringField('Choice A', validators=[DataRequired()])
    choice2 = StringField('Choice B', validators=[DataRequired()])
    choice3 = StringField('Choice C', validators=[DataRequired()])
    choice4 = StringField('Choice D', validators=[DataRequired()])
    correct_answer = RadioField('Correct Answer', choices=[('1', 'Choice A'), ('2', 'Choice B'), ('3', 'Choice C'), ('4', 'Choice D')], validators=[DataRequired()])
    submit = SubmitField('Submit')