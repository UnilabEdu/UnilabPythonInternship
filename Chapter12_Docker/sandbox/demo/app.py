from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    my_innerhtml = "<h1> Running from Docker </h1>"
    return my_innerhtml


if __name__ == "__main__":
    app.run(host="0.0.0.0")
