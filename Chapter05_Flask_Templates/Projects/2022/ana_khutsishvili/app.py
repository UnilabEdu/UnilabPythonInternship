from flask import Flask, render_template, url_for
app = Flask(__name__)

books = [
    {
        'author': 'Alan Moore',
        'title': 'Watchmen',
        'description': 'First book description',
        'date_published': '1986'
    },
    {
        'author': 'J. K. Rowling',
        'title': 'Harry Potter',
        'description': 'Second book description',
        'date_published': '1997'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', books=books)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
