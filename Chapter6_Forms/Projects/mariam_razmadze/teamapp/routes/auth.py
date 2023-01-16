from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user, login_user, logout_user, login_required
from ..import login_manager
from ..forms import LoginForm, RegisterForm, ValidationError
from werkzeug.security import check_password_hash
import requests



from ..extensions import db
from ..models import User

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
        unhashed_password=request.form['password']
        user=User.query.filter_by(name=name).first()
        if user:
            if check_password_hash(user.password, unhashed_password):
                login_user(user)
                return redirect(url_for('main.index'))

    return render_template('login.html', form=form, public_key=PUBLIC_KEY)



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
        name=request.form['name']
        unhashed_password=request.form['password']
        user=User(name=name, unhashed_password=unhashed_password, intern=True, junior=False, senior=False, admin=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form, public_key=PUBLIC_KEY)




