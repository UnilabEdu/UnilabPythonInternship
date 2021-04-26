from flask import Blueprint, request, render_template, redirect
from flask_login import login_required, current_user
from datetime import datetime
from app.posts.forms import PostForm
from app.models import PostsModel, UserModel
from app.tools.check_auth import check_auth
from app.tools.save_file import save_file
from app.tools.nav_link_list import generate_pages

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates'
                            )


# server:port/blueprint_prefix/add
@posts_blueprint.route('/', methods=['GET', 'POST'])
def list_posts():
    """
    shows all posts and lets signed-in users post a picture, text or both
    """
    form_post = PostForm()
    all_posts = PostsModel.query.all()
    authors = UserModel

    if request.method == 'POST' and check_auth():
        if form_post.text.data or form_post.media.data:
            text = form_post.text.data
            media = form_post.media.data
            time = datetime.now()

            if media:
                media = save_file(current_user.username, media, 'post_uploads')  # saves file to directory, returns filename

            PostsModel.add(time, text, media, current_user.id)

        return redirect('/posts')

    else:
        return render_template('posts.html', pages=generate_pages(), form=form_post, all_posts=all_posts, authors=authors)
