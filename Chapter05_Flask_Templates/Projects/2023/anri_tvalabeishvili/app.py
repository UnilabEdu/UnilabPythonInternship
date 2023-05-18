from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("pages/about.html")

@app.route('/game_store')
def game_store():
    return render_template("pages/Games_store.html")

    
@app.route('/gift_Cards')
def gift_Cards():
    return render_template("pages/about.html")

@app.route('/P2P')
def P2P():
    return render_template("pages/about.html")
    

    
if __name__ == "__main__":
    app.run(debug=True)