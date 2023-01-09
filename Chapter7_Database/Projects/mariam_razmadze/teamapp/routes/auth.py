from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user
from ..import login_manager
from werkzeug.security import check_password_hash


from ..extensions import db
from ..models import User

auth=Blueprint('auth', __name__)

# @login_manager.user_loader
@auth.route('/register', methods=['GET', 'POST'])
def register():
    names=[]
    users=User.query.all()
    for user in users:
        names.append(user.name)
    error_message=''
    if request.method=='POST':
        name=request.form['name']
        unhashed_password=request.form['password']
        user=User(name=name, unhashed_password=unhashed_password, intern=True, junior=False, senior=False, admin=False)
        error_message=""
        if user.name in names:
            error_message="User with that username already exists, sorry ❕"
            # return redirect(url_for('auth.login'))
        
        if not error_message:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

            
    return render_template('register.html',  error_message=error_message)

@login_manager.user_loader
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error_message=''
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']

        user=User.query.filter_by(name=name).first()

        error_message=""

        if not user or not check_password_hash(user.password, password):
            error_message="Your password is incorrect or this account doesn't exist ❕"
        
        if not error_message:
            login_user(user)
            return redirect(url_for('main.index'))
    

    return render_template('login.html', error_message=error_message)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



