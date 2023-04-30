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
    return render_template('home.html', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user=get_current_user()
    if request.method=='POST':
        db=get_db()
        hashed_password=generate_password_hash(request.form['password'], method='sha256')
        db.execute('insert into users(name, password, senior, junior, intern, admin) values (?, ?, ?, ?, ?, ?)', 
        [request.form['name'], hashed_password, '0', '0', '0', '0'])
        db.commit()
        session['user']=request.form['name']
        return redirect(url_for('index'))
    return render_template('register.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user=get_current_user()
    if request.method=='POST':
        db=get_db()

        name=request.form['name']
        password=request.form['password']
        user_cur=db.execute('select id, name, password from users where name=?', [name])
        user_res=user_cur.fetchone()
        # return'<h1>{}</h1>'.format(user_res['password'])
        # return "<h1>Username: {} Password: {}".format(request.form['name'], request.form['password'])

        if check_password_hash(user_res['password'], password):
            session['user']=user_res['name']
            return redirect(url_for('index'))
        else:
            return'<h1>Password is not correct</h1>'
    return render_template('login.html', user=user)

@app.route('/question')
def question():
    user=get_current_user()
    return render_template('question.html', user=user)

@app.route('/answer')
def answer():
    user=get_current_user()
    return render_template('answer.html', user=user)

@app.route('/ask')
def ask():
    user=get_current_user()
    return render_template('ask.html', user=user)

@app.route('/unanswered')
def unanswered():
    user=get_current_user()
    return render_template('unanswered.html', user=user)

@app.route('/users', methods=['GET', 'POST'])
def users():
    user=get_current_user()
    db=get_db()
    users_cur=db.execute('select id, name, senior, junior, intern, admin from users')
    users_res=users_cur.fetchall()
    # return(str(len(users_res)))

    if request.method=="POST":
        db=get_db()
        lst=[]
        for i in users_res:
            ind=str(i[0])
            lst.append(ind)
            for j in lst:
                status=request.form[j]

            if status=='0':
                db.execute('update or ignore users set senior=1, junior=0, intern=0 where id=?', j)
                db.commit()
            elif status=='1':
                db.execute('update or ignore users set senior=0, junior=1, intern=0 where id=?', j)
                db.commit()
            elif status=='2':
                db.execute('update or ignore users set senior=0, junior=0, intern=1 where id=?', j)
                db.commit()
        
        # return str(lst)
                
              
            
            
                # if status=='0':
                #     db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j))
                #     db.commit()
                # elif status=='1':
                #     db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j))
                #     db.commit()
                # elif status=='2':
                #     db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j))
                #     db.commit()
        # return str(lst)
            # for j in lst:
            #     status=request.form[str(j[0])]
            #     # return str(i[0])
            #     if status=='0':
            #         db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j[0]))
            #         db.commit()
            #     elif status=='1':
            #         db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j[0]))
            #         db.commit()
            #     elif status=='2':
            #         db.execute('update users set senior=1, junior=0, intern=0 where id=?', str(j[0]))
            #         db.commit()
                
            
    # lst=[]
    # for i in users_res:
    #     lst.append(str(i[0]))
    # return str(lst)
    # return str(user['id'])
    # return str(users_res[0][1])
    # return str(users_res[1][1])
    # for i in users_res:
    #     return i['name']
        # for j in i:
        #     return str(j)


    # if request.method=="POST":
    #     status=request.form[str(user['id'])]

    
   
    return render_template('users.html', user=user, users=users_res)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ =='__main__':
    app.run(debug=True)


