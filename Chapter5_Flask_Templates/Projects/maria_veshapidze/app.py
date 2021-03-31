from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/<guestname>')
def home(guestname=None):
    return render_template("home_page.html", name=guestname)


@app.route('/about_us')
def about():
    return render_template("about_us.html")


@app.route('/contact_info')
def contact():
    return render_template("contact_info.html")


@app.route('/registration')
def registration():
    return render_template("registration.html")


if __name__ == '__main__':
    app.run(port=8085, debug=True)