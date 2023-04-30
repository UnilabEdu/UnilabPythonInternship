from flask import Flask, render_template, request, flash
from contact import EmailForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'topSecret'

pages = ("home", "gallery", "contact")

@app.route('/')
def home():
    return render_template("index.html", content="home")


@app.route('/<content>')
def content(content=None):
    if content.lower() not in pages:
        content = "not_found"

    return render_template("index.html", content=str(content))


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    step = True
    email = None
    name = None
    text = None

    form = EmailForm()

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        text = form.text.data

        print(f"email: {email}")
        print(f"name: {name}")
        print(f"text: {text}")

        step = False

    return render_template("index.html", content="contact", form=form, step=step)


if __name__ == '__main__':
    app.run(port=8080, debug=True)