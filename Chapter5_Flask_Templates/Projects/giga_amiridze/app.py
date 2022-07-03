from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/press')
def press():
    return render_template("press.html")

if __name__ == "__main__":
    app.run(port=7777, debug=True)