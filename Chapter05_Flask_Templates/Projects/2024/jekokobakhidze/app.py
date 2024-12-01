from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {"title": "Home Page", "message": "Welcome to our Flask site!"}
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
