from flask import Blueprint, render_template
from src.resources.pages import nav_bar_pages

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates/posts')

@posts_blueprint.route('/add')
def add():
    return render_template('add.html', pages=nav_bar_pages)

@posts_blueprint.route('/list')
def posts_list():
    return render_template('list.html', pages=nav_bar_pages)

@posts_blueprint.route('/update')
def update():
    return render_template('update.html', pages=nav_bar_pages)

@posts_blueprint.route('/delete')
def delete():
    return render_template('delete.html', pages=nav_bar_pages)
