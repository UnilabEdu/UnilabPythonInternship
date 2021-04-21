from app.models import UserModel
from flask import Blueprint, render_template, session, redirect, request, flash
from app.routes import pages_nav_list
from app.profiles.forms import RegisterForm
from werkzeug.utils import secure_filename
from app.resources.format_dob import dob_string_to_datetime, calculate_age
from app.resources.general_crud import save_to_db
from app import db


profiles_blueprint = Blueprint('profiles',
                               __name__,
                               template_folder='templates'
                               )


# server:port/blueprint_prefix/add
@profiles_blueprint.route('/')
def list_people():
    # viewed shows the number of already viewed people (on previous pages)
    people_list = UserModel.query.all()
    return render_template('people.html', pages=pages_nav_list, people_list=people_list)


# server:port/blueprint_prefix/add
@profiles_blueprint.route('/profile', methods=['GET', 'POST'])
@profiles_blueprint.route('/profile/<username>')
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
                        x.data.save(f'app/static/uploads/profile_pictures/{picture_title}')
                        x.data = picture_title

                    # temporary, just for testing (to avoid circular imports)
                    save_to_db(target_user, x.name, x.data)

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
