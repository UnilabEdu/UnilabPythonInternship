from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    print(url_for('home'))
    return render_template('home.html')

@app.route('/about/')
def about():
    print(url_for('about'))
    return render_template('about.html')

@app.route('/contact/')
def contact():
    print(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)