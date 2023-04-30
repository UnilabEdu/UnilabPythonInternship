from flask import Flask, render_template, request, flash

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


if __name__ == '__main__':
    app.run(port=8080, debug=True)