from flask import Flask, render_template, url_for, redirect
from forms import Signin, UploadFilm
from flask_sqlalchemy import SQLAlchemy
from os import path
from uuid import uuid4

base_directory = path.abspath(path.dirname(__file__))
UPLOAD_PATH = path.join(base_directory, "uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(base_directory, 'database.db')

db = SQLAlchemy(app)

from models import Film

films = [
    {
        "name": "Sound of Metal",
        "cover": "https://a.ltrbxd.com/resized/film-poster/4/3/2/0/0/4/432004-sound-of-metal-0-1000-0-1500-crop.jpg?v=289acd955b"
    },
    {
        "name": "Memento",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/v1/3q/s4/aa/memento-0-1000-0-1500-crop.jpg?v=80f0732247"
    },
    {
        "name": "La Haine",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/6/8/4/51684-la-haine-0-1000-0-1500-crop.jpg?v=b6677cc136"
    },
    {
        "name": "The Social Network",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/nw/cm/pa/ai/sGQv3ZMZBDBnl3z42Q0mEQ5uiDe-0-1000-0-1500-crop.jpg?v=54ee59f7cd"
    },
    {
        "name": "City of God",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/5/2/3/51523-city-of-god-0-1000-0-1500-crop.jpg?v=7517ea94ce"
    },
    {
        "name": "Do the Right Thing",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/zm/fz/vn/ie/obNQLtdeJy3IiKnExWoWBJH8V67-0-1000-0-1500-crop.jpg?v=b4926532f8"
    },
    {
        "name": "Blade Runner",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/85/io/38/dz/vfzE3pjE5G7G7kcZWrA3fnbZo7V-0-1000-0-1500-crop.jpg?v=0d5de70f0d"
    },
    {
        "name": "Pulp Fiction",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/4/4/4/51444-pulp-fiction-0-1000-0-1500-crop.jpg?v=dee19a8077"
    }
]


@app.route('/home')
def home():
    return render_template('home.html', films=films)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    print(url_for('home'))
    form = Signin()
    if form.validate_on_submit():
        print(f"Email: {form.email.data}, Remember me: {form.remember_me.data}")
        return redirect(url_for('home'))
    return render_template('sign_in.html', form=form)


@app.route('/upload_film', methods=['GET', 'POST'])
def upload_film():
    form = UploadFilm()
    if form.validate_on_submit():
        cover = form.cover.data
        filename, file_extension = path.splitext(cover.filename)
        filename = str(uuid4())
        directory = path.join(UPLOAD_PATH, f"{filename}{file_extension}")
        cover.save(directory)
        film = Film(title=form.title.data, director=form.director.data, genre=form.genre.data, release_date=form.release_date.data, cover=filename)
        db.session.add(film)
        db.session.commit()
    return render_template('upload_movie.html', form=form)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)