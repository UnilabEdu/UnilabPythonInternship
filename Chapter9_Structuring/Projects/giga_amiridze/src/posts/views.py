from flask import Blueprint, render_template, redirect, url_for
from src.posts.forms import AddPost
from src.resources.pages import nav_bar_pages

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates/posts')

@posts_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddPost()

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        return redirect(url_for('posts.posts_list'))

    return render_template('add.html', pages=nav_bar_pages, form=form)

@posts_blueprint.route('/list')
def posts_list():
    return render_template('list.html', pages=nav_bar_pages)

@posts_blueprint.route('/update')
def update():
    return render_template('update.html', pages=nav_bar_pages)

@posts_blueprint.route('/delete')
def delete():
    return render_template('delete.html', pages=nav_bar_pages)
