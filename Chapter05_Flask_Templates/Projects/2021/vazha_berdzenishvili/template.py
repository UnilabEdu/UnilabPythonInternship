from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/registration')
def registration():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/store')
def store():
    return render_template('store.html')


if __name__ == "__main__":
    app.run(debug=True, port=8880)
