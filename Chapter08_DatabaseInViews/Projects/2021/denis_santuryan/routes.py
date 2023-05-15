from flask import render_template, url_for, session, redirect, flash, request
from forms import SignInForm, RegisterForm, PostForm
from app import app, UserModel, PostsModel, db
from general_crud import create, update, delete
from werkzeug.utils import secure_filename
from datetime import datetime, date
from format_dob import calculate_age, dob_string_to_datetime


pages_nav_list = [
    ("list_posts", "პოსტები"),
    ("list_people", "ხალხი"),
    ("list_pages", "გვერდები"),
    ("auth", "შესვლა")
]


@app.route('/timeline', methods=['GET', 'POST'])
def list_posts():
    user = None
    form_post = PostForm()
    all_posts = PostsModel.query.all()
    authors = UserModel

    try:
        if session['username']:
            user = UserModel.query.filter_by(username=session['username']).first()
            if request.method == 'POST':
                if form_post.text.data is None and form_post.media.data is None:
                    pass
                else:
                    text = form_post.text.data
                    media = form_post.media.data
                    time = datetime.now()
                    if media:
                        media_title = secure_filename(f'{user.username}_{media.filename}')
                        media.save(f'static/post_uploads/{media_title}')
                    else:
                        media_title = None
                    received_data = (time, text, media_title, user.id)
                    create(received_data, PostsModel)
                    return redirect('/timeline')
    except:
        pass

    return render_template('posts.html', pages=pages_nav_list, user=user, form=form_post, all_posts=all_posts, authors=authors)


@app.route('/people')
def list_people():
    # viewed shows the number of already viewed people (on previous pages)
    people_list = UserModel.query.all()
    return render_template('people.html', pages=pages_nav_list, people_list=people_list)


@app.route('/pages')
def list_pages():
    return render_template('placeholder.html', pages=pages_nav_list)


@app.route('/', methods=['GET', 'POST'])
def auth():
    show_flash = False

    try:
        if session['username'] is not None:  # if already logged in, redirects to user's profile
            pages_nav_list[3] = ("profile", session['username'])
            return redirect('/profile')
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
                    pages_nav_list[3] = ("profile", session['username'])
                    return redirect(url_for('profile'))

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
                    picture.save(f'static/profile_pictures/{picture_title}')

                # add everything to DB
                received_data = (username, name_first, name_last, email, phone, dob, age, sex, password, picture_title)
                create(received_data, UserModel)

                # automatically log in
                session['email'] = email  # used to display where a confirmation message would be sent
                session['username'] = username  # used to determine if logged in
                pages_nav_list[3] = ("profile", session['username'])
                show_flash = True
                flash('რეგისტრაცია წარმატებით დასრულდა!', 'alert-green')
                return redirect(url_for('success_register'))

        else:  # When data didn't pass WTForms validators
            show_flash = True
            flash('მონაცემები არასწორადაა შეყვანილი. თავიდან სცადეთ.', 'alert-yellow')

    return render_template('auth.html', pages=pages_nav_list, form_sign_in=form_sign_in, form_register=form_register, show_flash=show_flash)


@app.route('/profile', methods=['GET', 'POST'])
@app.route('/profile/<username>')
def profile(username=None):
    show_flash = True

    if request.method == 'POST':
        form_register = RegisterForm()
        target_user = UserModel.query.filter_by(username=session['username']).first()
        if form_register.password.data == target_user.password:
            formatted_date = dob_string_to_datetime(form_register.dob.data)
            received_data = []
            for x in set(form_register):
                if x.name == 'dob':
                    x.data = formatted_date
                    setattr(target_user, 'age', calculate_age(x.data))

                if x.data != '' and x.data is not None and x.name in target_user.__table__.c:
                    if x.name == 'picture':
                        picture_title = secure_filename(f'{session["username"]}_{x.data.filename}')
                        x.data.save(f'static/profile_pictures/{picture_title}')
                        x.data = picture_title

                    # target_user.update(x.name, x.data)
                    setattr(target_user, x.name, x.data)
                    db.session.commit()
            flash('მონაცემები წარმატებით განახლდა', 'alert-green')

        else:
            flash('პაროლი არასწორია – მონაცემები არ განახლდა', 'alert-red')

        return render_template('my_profile.html', pages=pages_nav_list, show_flash=show_flash, user=target_user, form_register=RegisterForm())

    elif username is None:
        try:
            if session['username'] is None:
                return redirect('/')
        except:
            return redirect('/')
        else:
            user = UserModel.query.filter_by(username=session['username']).first()
            return render_template('my_profile.html', pages=pages_nav_list, show_flash=show_flash, user=user, form_register=RegisterForm())
    else:
        user = UserModel.query.filter_by(username=username).first()
        return render_template('people_profile.html', pages=pages_nav_list, show_flash=show_flash, user=user)


@app.route('/success_register')
def success_register():
    return render_template('success_register.html', pages=pages_nav_list)


@app.route('/logoff')
def logoff():
    session['username'] = None
    pages_nav_list[3] = ("auth", "შესვლა")
    return redirect('/')
