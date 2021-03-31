from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'cannottellthiskey'


menu = [{"name": "Home", "url": "home"},
        {"name": "About author", "url": "about"},
        {"name": "Contact", "url": "contact"}]


@app.route('/')
@app.route('/home')
def home():
    return render_template("hiking_routes.html", menu=menu)


@app.route('/about')
def about():
    return render_template("about.html", menu=menu)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2 and len(request.form['email']) > 6 and len(request.form['message']) > 5:
            flash('Message sent', category='success')
        else:
            flash('Message error', category='error')
    return render_template("contact.html", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)