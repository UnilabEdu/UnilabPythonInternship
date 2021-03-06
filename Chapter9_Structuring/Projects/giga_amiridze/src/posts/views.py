from flask import Blueprint, render_template, redirect, url_for
from src.posts.forms import AddPost, DeletePost
from src.resources.pages import nav_bar_pages
from src.models import Post

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates/posts')

@posts_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddPost()

    if form.validate_on_submit():
        title = form.title.data
        post_content = form.post.data

        post = Post()
        post.create(title=title, post=post_content, commit=True)
        return redirect(url_for('posts.posts_list'))

    return render_template('add.html', pages=nav_bar_pages, form=form)

@posts_blueprint.route('/list')
def posts_list():
    db_list = Post.read_all()
    return render_template('list.html', pages=nav_bar_pages, posts=db_list)

@posts_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    form = AddPost()

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        post = Post.read(title=title)
        post.create(title=title, post=post, commit=True)
        return redirect(url_for('posts.posts_list'))

    return render_template('update.html', pages=nav_bar_pages, form=form)

@posts_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeletePost()

    if form.validate_on_submit():
        post_id = form.post_id.data

        post = Post.query.get(post_id)
        post.delete_from_db()
        return redirect(url_for('posts.posts_list'))

    return render_template('delete.html', pages=nav_bar_pages, form=form)
