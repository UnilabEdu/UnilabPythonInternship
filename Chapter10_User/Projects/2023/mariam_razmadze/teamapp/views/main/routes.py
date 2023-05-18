from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import or_, desc
from teamapp.models.question import Question
from teamapp.models.user import User, UserRole
from teamapp.utils import admin_required
from .forms import AnswerForm, AskForm
from teamapp import db

main=Blueprint('main', __name__, template_folder="templates")

@main.route('/')
def index():
    questions=Question.query.filter(Question.answer!= None).order_by(desc(Question.id)).all()
    lst=[]
    act=0
    for i in questions:
        lst.append(i.id)
    
    if len(lst)>=1:
        act=max(lst)

    context={
        'questions':questions, 
        'act': act, 
    }

    return render_template('main/about.html', **context)




@main.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    form=AskForm()
    if form.validate_on_submit():
        question=request.form['textarea']
        mentor=request.form['options']
        question=Question(question=question, mentor_id=mentor, asked_by_id=current_user.id)
            
        question.create()
        print('submitted')
        return redirect(url_for('main.index'))
    return render_template('main/ask.html', form=form)



@main.route('/unanswered')
@login_required
def unanswered():
    unanswered_questions=Question.query.filter_by(mentor_id=current_user.id).filter(Question.answer==None).order_by(desc(Question.id)).all()
    lst=[]
    act=0
    for i in unanswered_questions:
        lst.append(i.id)
    
    if len(lst)>=1:
          act=max(lst)
   

    context={
        'unanswered_questions': unanswered_questions, 
        'act': act
    }

    return render_template('main/unanswered.html', **context)


@main.route('/answer/<int:question_id>', methods=['GET', 'POST'])
@login_required
def answer(question_id):
    form=AnswerForm()
    question=Question.query.get_or_404(question_id)

    if request.method=='POST':
        question.answer=request.form['textarea']
        question.save()


        return redirect(url_for('main.unanswered'))

    context={
        'question': question
    }

    return render_template('main/answer.html', **context, form=form)




@main.route('/question/<int:question_id>')
def question(question_id):
    question=Question.query.get_or_404(question_id)

    context={
        'question': question
    }

    return render_template('main/question.html', **context)




        


 