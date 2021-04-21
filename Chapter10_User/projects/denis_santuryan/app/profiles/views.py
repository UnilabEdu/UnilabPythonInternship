from app.models import UserModel
from flask import Blueprint, render_template, redirect, request, flash
from app.profiles.forms import RegisterForm
from app.resources.format_dob import dob_string_to_datetime, calculate_age
from app.resources.general_crud import save_to_db
from app.resources.nav_link_list import generate_pages
from flask_login import current_user
from app.resources.save_file import save_file
from app.resources.check_auth import check_auth

profiles_blueprint = Blueprint('profiles',
                               __name__,
                               template_folder='templates'
                               )


# server:port/blueprint_prefix/add
@profiles_blueprint.route('/')
def list_people():
    # viewed shows the number of already viewed people (on previous pages)
    people_list = UserModel.query.all()
    return render_template('people.html', pages=generate_pages(), people_list=people_list)


# server:port/blueprint_prefix/add
@profiles_blueprint.route('/profile', methods=['GET', 'POST'])
@profiles_blueprint.route('/profile/<username>')
def profile(username=None):

    if request.method == 'POST':
        form_register = RegisterForm()
        if current_user.check_password(form_register.password.data):
            formatted_date = dob_string_to_datetime(form_register.dob.data)
            for x in set(form_register):
                if x.name == 'dob':
                    x.data = formatted_date
                    setattr(current_user, 'age', calculate_age(x.data))

                if x.data and x.data != '' and x.name in current_user.__table__.c:
                    if x.name == 'picture':
                        x.data = save_file(current_user.username, x.data, 'profile_pictures')  # saves file to directory, returns filename

                if x.name != 'password':
                    # temporary, just for testing (to avoid circular imports)
                    save_to_db(current_user, x.name, x.data)

            flash('მონაცემები წარმატებით განახლდა', 'alert-green')

        else:
            flash('პაროლი არასწორია – მონაცემები არ განახლდა', 'alert-red')

        return render_template('my_profile.html', pages=generate_pages(), form_register=RegisterForm())

    elif username:
        user = UserModel.find_by_username(username)
        return render_template('people_profile.html', pages=generate_pages())

    else:
        if check_auth():
            return render_template('my_profile.html', pages=generate_pages(), form_register=RegisterForm())

    return redirect('/')

