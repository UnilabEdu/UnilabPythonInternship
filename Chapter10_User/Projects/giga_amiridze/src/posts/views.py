from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from src.resources.pages import pages
from src.posts.forms import AddPost, DeletePost
from src.models import Post

posts_blueprint = Blueprint('post',
                            __name__,
                            template_folder='templates/posts'
                            )

@posts_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddPost()

    if form.validate_on_submit():
        title = form.title.data
        post_content = form.title.data

        post = Post()
        post.create(title=title, post=post_content, commit=True)
        return redirect(url_for('post.list'))

    return render_template('add.html', pages=pages, form=form)

@posts_blueprint.route('/list')
@login_required
def list():
    db_list = Post.read_all()
    return render_template('list.html', pages=pages, posts=db_list)

@posts_blueprint.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    form = AddPost()

    if form.validate_on_submit():
        title = form.title.data
        post_content = form.post.data

        post = Post.read(title=title)
        post.create(title=title, post=post_content, commit=True)
        return redirect(url_for('post.list'))

    return render_template('update.html', pages=pages, form=form)

@posts_blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeletePost()

    if form.validate_on_submit():
        post_id = form.post_id.data

        post = Post.query.get(post_id)
        post.delete_from_db()
        return redirect(url_for('post.list'))

    return render_template('delete.html', pages=pages, form=form)
