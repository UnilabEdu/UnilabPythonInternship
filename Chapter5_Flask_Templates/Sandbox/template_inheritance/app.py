from flask import Flask, render_template

serverPort = 8081

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("child.html")


if __name__ == '__main__':
    app.run(port=serverPort, debug=True)
