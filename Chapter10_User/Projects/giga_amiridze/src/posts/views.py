from flask import Blueprint, render_template

posts_blueprint = Blueprint('post',
                            __name__,
                            template_folder='templates/posts'
                            )

@posts_blueprint.route('/add')
def add():
    return render_template('add.html')

@posts_blueprint.route('/list')
def list():
    return render_template('list.html')

@posts_blueprint.route('/update')
def update():
    return render_template('update.html')

@posts_blueprint.route('/delete')
def delete():
    return render_template('delete.html')
