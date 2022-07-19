from flask import Blueprint, render_template

webpages_blueprint = Blueprint('webpages',
                               __name__,
                               template_folder='templates/main')


@webpages_blueprint.route('/')
def dashboard():
    return render_template("main.html")


@webpages_blueprint.route('/products')
def products():
    return render_template("products.html")


@webpages_blueprint.route('/flipacoin')
def flipacoin():
    return render_template("flipacoin.html")

@webpages_blueprint.route('/profile_page')
def profile_page():

    return render_template("profile_page.html")
