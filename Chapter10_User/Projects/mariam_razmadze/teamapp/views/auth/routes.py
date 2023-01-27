from flask import Blueprint, render_template, request, redirect, url_for, abort, session
from flask_login import login_user, logout_user
from teamapp import login_manager
from .forms import LoginForm, RegisterForm
from werkzeug.security import check_password_hash
import requests

from teamapp.models.user import User

PUBLIC_KEY='6Le2fvsjAAAAAGS6PR5pM9tIzKXIpZbppK-k5IEx'
PRIVATE_KEY='6Le2fvsjAAAAAGJpxYuW-nThZyuoX6j0NmMEY2IK'
VERIFY_URL= 'https://www.google.com/recaptcha/api/siteverify'

auth=Blueprint('auth', __name__)

login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()

    if request.method=='POST':
        secret_response=request.form['g-recaptcha-response']
        print(request.form)
        print('Mariam')
        verify_response=requests.post(url=f'{VERIFY_URL}?secret={PRIVATE_KEY}&response={secret_response}').json()
        if verify_response['success']==False or verify_response['score']<0.5:
            abort(401)
        print(verify_response)

    if form.validate_on_submit():
        name=request.form['name']
        user=User.query.filter_by(name=name).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if 'next' in session:
                next=session['next'] 
                print(next)
                if next == None:
                   return redirect(url_for('main.index'))  
                return redirect(next) 
            else: 
                return redirect(url_for('main.index'))        

    session['next']=request.args.get('next')
    return render_template('auth/login.html', form=form, public_key=PUBLIC_KEY)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    if request.method=='POST':
        secret_response=request.form['g-recaptcha-response']
        print(request.form)
        print('Mariam')
        verify_response=requests.post(url=f'{VERIFY_URL}?secret={PRIVATE_KEY}&response={secret_response}').json()
        if verify_response['success']==False or verify_response['score']<0.5:
            abort(401)
        print(verify_response)
    if form.validate_on_submit():
        name=form.name.data
        password=form.password.data
        user=User(name=name, password=password)
        user.create()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, public_key=PUBLIC_KEY)




