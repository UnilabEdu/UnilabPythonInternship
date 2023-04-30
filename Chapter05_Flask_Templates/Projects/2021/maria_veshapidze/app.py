from flask import Flask, render_template, url_for

app = Flask(__name__)

nav_bar_pages_list = (
    ("home", "Home",),
    ("about", "About us"),
    ("contact", "Contact Info"),
    ("registration", "Registration")
)


@app.route('/')
@app.route('/<guestname>')
def home(guestname=None):
    return render_template("home_page.html", name=guestname, pages=nav_bar_pages_list)


@app.route('/about_us')
def about():
    return render_template("about_us.html", pages=nav_bar_pages_list)


@app.route('/contact_info')
def contact():
    return render_template("contact_info.html", pages=nav_bar_pages_list)


@app.route('/registration')
def registration():
    return render_template("registration.html", pages=nav_bar_pages_list)


if __name__ == '__main__':
    app.run(port=8085, debug=True)