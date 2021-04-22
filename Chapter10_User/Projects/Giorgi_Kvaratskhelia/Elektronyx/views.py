"""
Routes and views for the web application
"""
from flask import render_template, flash, request, url_for, redirect
from flask_login import login_user, logout_user, login_required

from Elektronyx.models import *
from Elektronyx.forms import *
from Elektronyx import app, admin

featured_items = (
    GPU.find_by_name("GeForce GTX 1070"),
    GPU.find_by_name("GeForce RTX 3090"),
    GPU.find_by_name("GeForce GTX 1660 Super"),
    CPU.find_by_name("Core i9-10900K"),
    CPU.find_by_name("Ryzen 8 2700X"),
    Motherboard.find_by_name("ROG STRIX X299-E"),
    Motherboard.find_by_name("ROG STRIX Z490-E"),
    PSU.find_by_name("ROG Thor 850"),
    PSU.find_by_name("HX1000"),
    RAM.find_by_name("TridentZ Series"),
)

promo_items = (
    ('180.0', Case.find_by_name('Evolv X')),
    ('110.0', Case.find_by_name('H400i')),
    ('149.9', Storage.find_by_name('Barracuda 8TB')),
    ('50.0', Storage.find_by_name('Ultrastar 7K4000'))
)

@app.route('/')
def home():
    return render_template("index.html", featured_items=featured_items, promo_items=promo_items)


@app.route('/catalog/<string:product_type>')
def catalog(product_type):
    if product_type == 'case':
        data = Case.get_all()
    elif product_type == 'motherboard':
        data = Motherboard.get_all()
    elif product_type == "cpu":
        data = CPU.get_all()
    elif product_type == "gpu":
        data = GPU.get_all()
    elif product_type == "psu":
        data = PSU.get_all()
    elif product_type == "ram":
        data = RAM.get_all()
    elif product_type == "storage":
        data = Storage.get_all()

    return render_template("catalog.html", catalog_data=data, product_type=product_type)


@app.route('/catalog/<string:product_type>/<string:product_name>')
def item(product_type, product_name):

    if product_type == 'case':
        data = Case.find_by_name(product_name)
    elif product_type == 'motherboard':
        data = Motherboard.find_by_name(product_name)
    elif product_type == "cpu":
        data = CPU.find_by_name(product_name)
    elif product_type == "gpu":
        data = GPU.find_by_name(product_name)
    elif product_type == "psu":
        data = PSU.find_by_name(product_name)
    elif product_type == "ram":
        data = RAM.find_by_name(product_name)
    elif product_type == "storage":
        data = Storage.find_by_name(product_name)
    
    return render_template("item.html", product=vars(data))


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    login_form = LoginForm()

    if register_form.register.data and register_form.validate():

        check_email = User.find_by_email(register_form.email.data)
        check_user = User.find_by_user(register_form.username.data)

        if check_email is None and check_user is None:
            user = User(register_form.email.data, register_form.username.data, register_form.password.data, 0)
            user.add_user()
            flash("User has been registered")

    if login_form.login.data and login_form.validate():
        user = User.find_by_user(login_form.username.data)
        if user is not None and user.check_password(login_form.password.data):
            login_user(user)

            previous_page = request.args.get('next')
            if previous_page is None:
                previous_page = url_for('home')

            return redirect(previous_page)

    return render_template('register.html', register_form=register_form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


admin.add_view(CustomModelView(User, db.session))
admin.add_view(CustomModelView(Case, db.session))
admin.add_view(CustomModelView(Motherboard, db.session))
admin.add_view(CustomModelView(CPU, db.session))
admin.add_view(CustomModelView(GPU, db.session))
admin.add_view(CustomModelView(RAM, db.session))
admin.add_view(CustomModelView(Storage, db.session))
admin.add_view(CustomModelView(PSU, db.session))

