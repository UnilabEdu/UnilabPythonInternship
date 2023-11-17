from flask import Flask, render_template, url_for



app = Flask(__name__, template_folder='templates')


anime_list = [
    {"img": "ebcd65fa9fb83580062e7052fa6ee5a5.jpe", "name": "JUJUTSU KAISEN", "text": "Sub|Dub"},
    {"img": "f154230aab3191aba977f337d392f812.jpe", "name": "One Piece", "text": "Subtitled"},
    {"img": "d458b9695157881b8b257226a2f68bb3.jpe", "name": "Mushoku Tensei: Jobless Reincarnation", "text": "Sub|Dub"},
    {"img": "f446d7a2a155c6120742978fb528fb82.jpe", "name": "Frieren: Beyond Journey's End", "text": "Sub|Dub"},
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", anime_list=anime_list)

@app.route('/genre')
def genre():
    return render_template("index.html")

@app.route('/browse')
def browse():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/animes')
def animes():
    return render_template('popular_animes.html', anime_list=anime_list)

@app.route('/animes/<int:id>')
def view_anime(id):
    chosen_anime= anime_list[id]
    return render_template("view_anime.html", anime=chosen_anime)




if __name__ == '__main__':
    app.run(debug=True)