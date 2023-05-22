from datetime import date

from flask import redirect, render_template, url_for, flash
from werkzeug.utils import secure_filename

from app import app, basedir
from app.forms import SignIn, ArticleForm
from app.models import db, Article


@app.route('/')
def index():
	form = SignIn()

	return render_template("index.html", form=form)


@app.route('/blog', methods=['GET', 'POST'])
def blog():
	form = ArticleForm()
	articles = Article.query.all()

	if form.validate_on_submit():
		filename = secure_filename(form.preview_img.data.filename)
		form.preview_img.data.save(basedir + '\\static\\uploads\\' + filename)

		article = Article(
			title=form.title.data,
			body=form.body.data,
			date=date.today(),
			preview_img='/uploads/' + form.preview_img.data.filename
		)

		db.session.add(article)
		db.session.commit()

		flash("Article Added", "success")
		return redirect(url_for('blog'))

	return render_template("blog.html", articles=articles, form=form)


@app.route('/sign-in', methods=['POST'])
def sign_in():
	form = SignIn()

	if form.validate_on_submit():
		print(form.username.data, form.password.data, form.remember.data)
		flash("Successfully signed in!", "success")

	return redirect(url_for('index'))


@app.route('/sign-up')
def sign_up():
	return render_template("signup.html")
