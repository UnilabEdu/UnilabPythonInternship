from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user

from app.commands import app
from app.database import db
from app.models import UserModel
from app.profiles.forms import SignInForm, RegisterForm
from app.tools.check_auth import check_auth
from app.tools.format_dob import calculate_age, dob_string_to_datetime
from app.tools.general_crud import create
from app.tools.nav_link_list import generate_pages
from app.tools.save_file import save_file


@app.route('/pages')
def list_pages():
    return render_template('placeholder.html', pages=generate_pages())


@app.route('/', methods=['GET', 'POST'])
def auth():
    form_sign_in = SignInForm()
    form_register = RegisterForm()

    if check_auth():
        return redirect(url_for('profiles.profile'))

    if request.method == 'POST':

        # Login Attempt
        if form_sign_in.validate_on_submit():
            target_account = None
            identifier = form_sign_in.identifier.data.lower()
            login_password = form_sign_in.login_password.data
            remember_me = form_sign_in.remember_me.data

            # Check if logging in through Email
            if UserModel.find_by_email(identifier):
                target_account = UserModel.find_by_email(identifier)

            # Check if logging in through Username
            elif UserModel.find_by_username(identifier):
                target_account = UserModel.find_by_username(identifier)

            #  Check Password only if the account was found either through Email or Username
            if target_account:
                if target_account.check_password(login_password):  # Successful log-in
                    flash('წარმატებით შეხვედით სისტემაში!', 'alert-green')

                    if remember_me:
                        login_user(target_account, remember=True)
                    else:
                        login_user(target_account)

                    #  redirect to a previously chosen link
                    if request.args.get('next'):
                        return redirect(request.args.get('next'))

                    else:
                        return redirect(url_for('profiles.profile'))

                else:  # Wrong Password
                    form_sign_in.login_password.data = ''
                    flash('პაროლი არასწორია', 'alert-yellow')

            else:  # Wrong Email or Username
                form_sign_in.identifier.data = ''
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
            if UserModel.find_by_username(username):
                success = False
                flash('იუზერნეიმი დაკავებულია', 'alert-yellow')
            elif UserModel.find_by_email(email):
                success = False
                flash('მეილი დაკავებულია', 'alert-yellow')

            if success:
                # check if picture was uploaded and save it
                picture_title = None
                picture = form_register.picture.data

                if picture:
                    picture_title = save_file(username, picture, 'profile_pictures')  # saves file to directory, returns filename

                # add everything to DB           # needs to be changed
                role = 3
                received_data = (username, name_first, name_last, email, phone, dob, sex, password, role, age, picture_title)
                create(received_data, UserModel)
                new_user = UserModel(*received_data)
                db.session.add(new_user)
                db.session.commit()

                flash('რეგისტრაცია წარმატებით დასრულდა!', 'alert-green')
                login_user(UserModel.find_by_username(username))

                return redirect(url_for('success_register'))

        else:  # When data didn't pass WTForms validators
            flash('მონაცემები არასწორადაა შეყვანილი. თავიდან სცადეთ.', 'alert-yellow')

    return render_template('auth.html', pages=generate_pages(), form_sign_in=form_sign_in, form_register=form_register)


@app.route('/success_register')
def success_register():
    return render_template('success_register.html', pages=generate_pages())


@app.route('/logoff')
def logoff():
    logout_user()
    flash('წარმატებით გამოხვედით სისტემიდან', 'alert-green')
    return redirect('/')
