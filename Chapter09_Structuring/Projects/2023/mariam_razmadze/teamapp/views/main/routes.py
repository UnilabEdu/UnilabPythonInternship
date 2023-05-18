from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import or_, desc
from teamapp.models.question import Question
from teamapp.models.user import User

from .forms import AnswerForm, AskForm, RadioForm

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
        'act': act
    }

    return render_template('main/home.html', **context)




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



@main.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    form=RadioForm
    users=User.query.filter_by(admin=False).all()

    context={
        'users': users
    }


    return render_template('main/users.html', **context, form=form)



    
@main.route('/assign', methods=['GET', 'POST'])
@login_required
def assign():
    if not current_user.admin:
        return redirect(url_for('main.index'))
    status=None
    form_status=None
    users=User.query.filter_by(admin=False).all()
    for user in users:
        if user.senior==1:
            status='0'
        elif user.junior==1:
            status='1'
        elif user.intern==1:
            status='2'
        form_status=request.form.get(str(user.id))
        if status!=form_status:
            status=form_status
            if status=='0':
                user.senior=1 
                user.junior=0
                user.intern=0
            
            elif status=='1':
                user.senior=0
                user.junior=1
                user.intern=0
            elif status=='2':
                user.senior=0
                user.junior=0
                user.intern=1
        user.save()
    return redirect(url_for('main.users'))
        



 