from flask import render_template, url_for, session, redirect, flash, request
from app.profiles.forms import SignInForm, RegisterForm
from app import app
from app.resources.general_crud import create
from werkzeug.utils import secure_filename
from app.resources.format_dob import calculate_age, dob_string_to_datetime
from app.models import UserModel


pages_nav_list = [
    ("posts.list_posts", "პოსტები"),
    ("profiles.list_people", "ხალხი"),
    ("list_pages", "გვერდები"),
    ("auth", "შესვლა")
]


@app.route('/pages')
def list_pages():
    return render_template('placeholder.html', pages=pages_nav_list)


@app.route('/', methods=['GET', 'POST'])
def auth():
    show_flash = False

    try:
        if session['username'] is not None:  # if already logged in, redirects to user's profile
            pages_nav_list[3] = ("profiles.profile", session['username'])
            return redirect('people/profile')
    except:
        pass

    form_sign_in = SignInForm()
    form_register = RegisterForm()

    if request.method == 'POST':

        # Login Attempt
        if form_sign_in.validate_on_submit():
            target_account = None
            identifier = form_sign_in.identifier.data.lower()
            login_password = form_sign_in.login_password.data

            # Check if logging in through Email
            if UserModel.query.filter_by(email=identifier).first():
                target_account = UserModel.query.filter_by(email=identifier).first()

            # Check if logging in through Username
            elif UserModel.query.filter_by(username=identifier).first():
                target_account = UserModel.query.filter_by(username=identifier).first()

            #  Check Password only if the account was found either through Email or Username
            if target_account:
                correct_password = target_account.password

                if login_password == correct_password:  # Successful log-in
                    show_flash = True
                    flash('წარმატებით შეხვედით სისტემაში!', 'alert-green')

                    # if remember_me was checked make session permanent
                    remember_me = form_sign_in.remember_me.data
                    if remember_me:
                        session.permanent = True
                    else:
                        session.permanent = False

                    session['username'] = target_account.username  # used to determine if logged in
                    pages_nav_list[3] = ("profiles.profile", session['username'])
                    return redirect(url_for('profiles.profile'))

                else:  # Wrong Password
                    form_sign_in.login_password.data = ''
                    show_flash = True
                    flash('პაროლი არასწორია', 'alert-yellow')

            else:  # Wrong Email or Password
                form_sign_in.login_password.data = ''
                show_flash = True
                flash('ამ მეილით ან იუზერნეიმით მომხმარებელი არ მოიძებნა', 'alert-yellow')

        # Register Attempt
        elif form_register.validate_on_submit():
            success = True
            # initialize received data
            username = form_register.username.data.lower()
            name_first = form_register.name_first.data
            name_last = form_register.name_last.data
            email = form_register.email.data.lower()
            phone = form_register.phone.data
            dob = dob_string_to_datetime(form_register.dob.data)
            age = calculate_age(dob)
            sex = form_register.sex.data
            password = form_register.password.data

            # check if the username and email are unique
            if UserModel.query.filter_by(username=username).first():
                success = False
                show_flash = True
                flash('იუზერნეიმი დაკავებულია', 'alert-yellow')
            elif UserModel.query.filter_by(email=email).first():
                success = False
                show_flash = True
                flash('მეილი დაკავებულია', 'alert-yellow')

            if success:
                # check if picture was uploaded and save it
                picture_title = None
                picture = form_register.picture.data
                if picture:
                    picture_title = secure_filename(f'{username}_{picture.filename}')
                    picture.save(f'app/static/uploads/profile_pictures/{picture_title}')

                # add everything to DB
                received_data = (username, name_first, name_last, email, phone, dob, age, sex, password, picture_title)
                create(received_data, UserModel)

                # automatically log in
                session['email'] = email  # used to display where a confirmation message would be sent
                session['username'] = username  # used to determine if logged in
                pages_nav_list[3] = ("profiles.profile", session['username'])
                show_flash = True
                flash('რეგისტრაცია წარმატებით დასრულდა!', 'alert-green')
                return redirect(url_for('success_register'))

        else:  # When data didn't pass WTForms validators
            show_flash = True
            flash('მონაცემები არასწორადაა შეყვანილი. თავიდან სცადეთ.', 'alert-yellow')

    return render_template('auth.html', pages=pages_nav_list, form_sign_in=form_sign_in, form_register=form_register, show_flash=show_flash)


@app.route('/success_register')
def success_register():
    return render_template('success_register.html', pages=pages_nav_list)


@app.route('/logoff')
def logoff():
    session['username'] = None
    pages_nav_list[3] = ("auth", "შესვლა")
    return redirect('/')
