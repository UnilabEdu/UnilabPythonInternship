from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home_page():
    return render_template('index.html')


@main.route('/about_us')
def about_us():
    return render_template('about.html')


@main.route('/contact_us')
def contact_us():
    return render_template('contact.html')