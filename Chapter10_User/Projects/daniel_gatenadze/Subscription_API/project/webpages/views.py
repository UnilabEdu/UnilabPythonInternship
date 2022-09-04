from flask import Blueprint, render_template, request, flash, Flask, redirect, url_for
from flask_login import login_required, current_user
from .webpages_forms import UserProfile, CheckoutForm
from project.extensions import db
from project.user.models import User
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from project import create_app

application = Flask(__name__)
UPLOAD_FOLDER = 'project/static/images'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

webpages_blueprint = Blueprint('webpages',
                               __name__,
                               template_folder='templates')


@webpages_blueprint.route('/')
def dashboard():
    return render_template("main.html")


@webpages_blueprint.route('/products')
def products():
    return render_template("products.html")


@webpages_blueprint.route('/flipacoin')
def flipacoin():
    return render_template("flipacoin.html")


@webpages_blueprint.route('/profile_page', methods=['GET', 'POST'])
@login_required
def profile_page():
    form = UserProfile()
    user_id = current_user.id
    name_to_update = User.query.get_or_404(user_id)
    if request.method == "POST":
        name_to_update.username = request.form['username']
        name_to_update.email = request.form['email']
        name_to_update.about = request.form['about']

        if request.files['profile_pic']:
            name_to_update.profile_pic = request.files['profile_pic']

            pic_filename = secure_filename(name_to_update.profile_pic.filename)
            pic_name = str(uuid.uuid1()) + '_' + pic_filename
            saver = request.files['profile_pic']
            name_to_update.profile_pic = pic_name
            try:
                db.session.commit()
                saver.save(os.path.join(application.config['UPLOAD_FOLDER'], pic_name))
                flash('Profile Updated')
                return render_template('profile_page.html',
                                       form=form,
                                       name_to_update=name_to_update)
            except:
                flash('Error!  Looks like there was a problem...try again!')
                return render_template("profile_page.html",
                                       form=form,
                                       name_to_update=name_to_update)
        else:
            db.session.commit()
            flash('Profile Updated')
            return render_template('profile_page.html',
                                   form=form,
                                   name_to_update=name_to_update)
    else:
        return render_template('profile_page.html',
                               form=form,
                               name_to_update=name_to_update,
                               user_id=user_id)
    return render_template('profile_page.html')


@webpages_blueprint.route('/checkout')
@login_required
def checkout():
    myform = CheckoutForm()
    if myform.validate_on_submit():
        return redirect(url_for('webpages.dashboard'))
    return render_template('checkout.html', form=myform)
