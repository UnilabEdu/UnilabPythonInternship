from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def home():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/img')
def img():
    return render_template("img.html")
@app.route('/video')
def video():
    return render_template("video.html")


if __name__ == '__main__':
    app.run(port=8085, debug=True)