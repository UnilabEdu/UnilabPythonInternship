from flask import redirect, render_template, request, url_for
from app import app
from app.forms import LoginForm, RegistrationForm, UpdateAccountForm, DeleteAccountForm
from wtforms.validators import ValidationError
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app.models import User, db
import bcrypt

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'




@app.before_first_request
def create_user():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@login_required
def index():
    if current_user.username == 'admin':
        return redirect(url_for('admin'))
    return render_template('blog/home.html')


@app.route('/admin')
def admin():
    return render_template('blog/admin.html')

@app.route('/list_user')
def list_user():
    users = User.query.all()
    return render_template('blog/list_user.html', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            user = User(form.username.data, form.email.data, form.password.data)
            user.create()
            return redirect(url_for('login'))
        else:
            return render_template('auth/register.htm', form=form)
    else:
        form = RegistrationForm()
        return render_template('auth/register.htm', form=form)

@app.route('/update_user', methods=['GET', 'POST'])
def update_user():

    if request.method == 'POST':
        form = UpdateAccountForm(request.form)
        if form.validate():
            user = User.query.filter_by(username=form.name.data).first()
            user.name = form.name.data
            user.email = form.email.data
            user.username = form.username.data
            user.update()
            return redirect(url_for('list_user'))
        else:
            return render_template('auth/update_user.html', form=form)
    else:
        form = UpdateAccountForm()
        return render_template('auth/update_user.html', form=form)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        form = DeleteAccountForm(request.form)
        print(form.name.data)
        if form.validate():
            user = User.query.filter_by(username=form.name.data).first()
            print(user)
            user.delete()
            return redirect(url_for('list_user'))
        else:
            return render_template('auth/delete_user.html', form=form)
    else:
        form = DeleteAccountForm()
        return render_template('auth/delete_user.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # print(current_user.is_authenticated)
    if request.method == 'POST':
        form = LoginForm(request.form)
        username = form.username.data
        password = form.password.data
        if form.validate():
            usera = User.query.filter_by(username=username).first()
            if usera:
                hashed_password = usera.password
                check_password = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
                if check_password:
                    login_user(usera)
                    return redirect(url_for('index'))
                else:
                    return render_template('auth/login.htm', form=form, error='Invalid username or password')
            return render_template('auth/login.htm', form=form, error='Invalid username or password')
        return render_template('auth/login.htm', form=form)
    
    if request.method == 'GET':
        form = LoginForm()
        return render_template('auth/login.htm', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegistrationForm()
        return render_template('auth/register.htm', form=form)
    
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        username = form.username.data
        password = form.password.data
        if form.validate():
            user = User.query.filter_by(username=username).first()
            if user:
                return render_template('auth/register.htm', form=form, error='Username already exists')
            
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User(username=form.username.data, password=hashed, email=form.email.data)
            user.create()
            return redirect(url_for('login'))
            
        return render_template('auth/register.htm', form=form, error=form.errors)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))