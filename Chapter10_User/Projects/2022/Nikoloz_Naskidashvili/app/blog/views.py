import os
from datetime import date

from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import current_user

from app.config import BASE_DIR_APP

from app.blog.forms import ArticleForm
from app.blog.models import Article


blog_blueprint = Blueprint(
		'blog',
		__name__,
		template_folder='templates/blog',
		url_prefix='/blog'
	)


@blog_blueprint.route('/', methods=['GET', 'POST'])
def blog():
	form = ArticleForm()
	articles = Article.read_all()
	article_model = Article()

	if form.validate_on_submit() and current_user.is_authenticated:
		filename = secure_filename(form.preview_img.data.filename)
		path_list = f"static,uploads,{filename}".split(",")
		print(os.path.join(BASE_DIR_APP, os.path.join(*path_list)))
		form.preview_img.data.save(os.path.join(BASE_DIR_APP, os.path.join(*path_list)))

		article_model.create(
			commit=True,
			title=form.title.data,
			body=form.body.data,
			date=date.today(),
			preview_img='/uploads/' + form.preview_img.data.filename
		)

		flash("Article Added", "success")
		return redirect(url_for('blog.blog'))

	return render_template("blog.html", articles=articles, form=form)
