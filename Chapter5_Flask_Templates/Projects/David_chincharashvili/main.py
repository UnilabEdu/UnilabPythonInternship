from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')


@app.route('/about_us')
def about():
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    data=json.loads(resp.text)
    return render_template('about.html', data=data)


@app.route('/contact_us')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)