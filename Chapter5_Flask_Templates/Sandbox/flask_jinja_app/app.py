from flask import Flask, render_template

serverPort = 8081

app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def home(username=None):
    return render_template("base.html", name=username)


if __name__ == '__main__':
    app.run(port=serverPort, debug=True)
