from flask import Flask, render_template, g, request, session, redirect, url_for
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_current_user():
    user_res = None
    if 'user' in session:
        user=session['user']
    
        db=get_db()
        user_cur=db.execute('select id, name, password, senior, junior, intern, admin from users where name=?', [user])
        user_res=user_cur.fetchone()
    
    return user_res

@app.route('/')
def index():
    user=get_current_user()
    db=get_db()
    act=0
    questions_cur=db.execute('select questions.id as question_id, questions.question_text,\
         askers.name as asker_name, askers.senior as asker_senior, askers.junior as asker_junior,\
        askers.intern as asker_intern, mentors.name as mentor_name, \
        mentors.senior as mentor_senior, mentors.junior as mentor_junior from questions join users as askers on askers.id= questions.asked_by_id join users\
             as mentors on mentors.id=questions.mentor_id where questions.answer_text is not null order by questions.id desc')
    questions_res=questions_cur.fetchall()
    lst=[]
    for q in questions_res:
        lst.append(int(q[0]))
    
    if len(lst)>=1:
        act=max(lst)
    return render_template('home.html', user=user, questions=questions_res, act=act)


@app.route('/register', methods=['GET', 'POST'])
def register():
    user=get_current_user()
    if request.method=='POST':
        db=get_db()
        already_exists_cur=db.execute('select id from users where name=?', [request.form['name']])
        already_exists=already_exists_cur.fetchone()

        if already_exists:
            return render_template('register.html', user=user, error="Sorry, that username already exists!")

        hashed_password=generate_password_hash(request.form['password'], method='sha256')
        db.execute('insert into users(name, password, senior, junior, intern, admin) values (?, ?, ?, ?, ?, ?)', 
        [request.form['name'], hashed_password, '0', '0', '0', '0'])
        db.commit()
        session['user']=request.form['name']
        return redirect(url_for('index'))
    return render_template('register.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    user=get_current_user()
    if request.method=='POST':
        db=get_db()
        name=request.form['name']
        password=request.form['password']
        user_cur=db.execute('select id, name, password from users where name=?', [name])
        user_res=user_cur.fetchone()

        if user_res:
            if check_password_hash(user_res['password'], password):
                session['user']=user_res['name']
                return redirect(url_for('index'))
            else:
               error="Your password is incorrect or this account doesn't exist ❕"
        else:
            error="Sorry, we couldn't find your account ❕"
    return render_template('login.html', user=user, error=error)

@app.route('/question/<question_id>')
def question(question_id):
    user=get_current_user()
    db=get_db()
    questions_cur=db.execute('select  questions.question_text, questions.answer_text,\
         askers.name as asker_name, askers.senior as asker_senior, askers.junior as asker_junior,\
        askers.intern as asker_intern,  mentors.name as mentor_name, mentors.senior as mentor_senior,\
        mentors.junior as mentor_junior from questions \
        join users as askers on askers.id= questions.asked_by_id\
        join users as mentors on mentors.id=questions.mentor_id where questions.id=?', [question_id])
    question=questions_cur.fetchone()
    return render_template('question.html', user=user, question=question)

@app.route('/answer/<question_id>', methods=['GET', 'POST'])
def answer(question_id):
    user=get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['intern']==1:
        return redirect(url_for('index'))
    db=get_db()

    if request.method=='POST':
        db.execute('update questions set answer_text=(?) where id=(?)', [request.form['answer'], question_id])
        db.commit()
        return redirect(url_for('unanswered'))
        
        # return '<h1>Question ID: {}, Answer: {}</h1>'.format(question_id, request.form['answer'])
    question_cur=db.execute('select id, question_text from questions where id =?', [question_id])
    question=question_cur.fetchone()
    return render_template('answer.html', user=user, question=question)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    user=get_current_user()
    if not user:
        return redirect(url_for('login'))

    db=get_db()
    if request.method=='POST':
        
        db.execute('insert into questions(question_text, asked_by_id, mentor_id) values (?, ?, ?)', [request.form['question'], user['id'], request.form['mentor']] )
        db.commit()
        # return 'QUESTION : {}, Mentor ID: {}'.format(request.form['question'], request.form['mentor'])
        return redirect(url_for('index'))
    
    mentor_cur=db.execute('select id, name from users where senior=1 OR junior=1')
    mentor_res=mentor_cur.fetchall()
    return render_template('ask.html', user=user, mentors=mentor_res)

@app.route('/unanswered')
def unanswered():
    user=get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['intern']==1:
        return redirect(url_for('index'))

    db=get_db()
    act=0
    
    questions_cur=db.execute('select questions.id, questions.question_text, \
    users.name, users.senior as user_senior, users.junior as user_junior, users.intern as user_intern\
    from questions join users on users.id=questions.asked_by_id \
    where questions.answer_text is null and questions.mentor_id=(?) order by questions.id desc', [user['id']])
    questions=questions_cur.fetchall()
    lst=[]
    for q in questions:
        lst.append(int(q[0]))
    
    if len(lst)>=1:
        act=max(lst)
    return render_template('unanswered.html', user=user, questions=questions, act=act)

@app.route('/users', methods=['GET', 'POST'])
def users():
    user=get_current_user()

    if not user:
        return redirect(url_for('login'))
    
    if user['admin']==0:
        return redirect(url_for('index'))
    db=get_db()
    users_cur=db.execute('select id, name, senior, junior, intern, admin from users')
    users_res=users_cur.fetchall()
    return render_template('users.html', user=user, users=users_res)

    
@app.route('/assign', methods=['GET', 'POST'])
def assign():
    user=get_current_user()

    if not user:
        return redirect(url_for('login'))
    if user['admin']==0:
        return redirect(url_for('index'))
    db=get_db()
    users_cur=db.execute('select id, name, senior, junior, intern, admin from users')
    users_res=users_cur.fetchall()
    status=None
    form_status=None
    for i in users_res:
        if str(i[2])=='1':
            status='0'
        elif str(i[3])=='1':
            status='1'
        elif str(i[4])=='1':
            status='2'
        if request.form.get(str(i[0])):
            form_status=request.form.get(str(i[0]))
            if status!=form_status:
                status=form_status

        if status:   
            if status=='0':
                db.execute('update or ignore users set senior=1, junior=0, intern=0 where id=?', str(i[0]))
          
            elif status=='1':
                db.execute('update or ignore users set senior=0, junior=1, intern=0 where id=?', str(i[0]))
                
            elif status=='2':
                db.execute('update or ignore users set senior=0, junior=0, intern=1 where id=?', str(i[0]))
            
            db.commit()
    return redirect(url_for('users'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ =='__main__':
    app.run(debug=True)

