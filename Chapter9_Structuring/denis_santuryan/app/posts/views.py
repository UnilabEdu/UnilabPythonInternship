from app.posts.forms import PostForm
from app.models import PostsModel, UserModel
from flask import Blueprint, session, request, render_template, redirect, url_for
from app.routes import pages_nav_list
from datetime import datetime
from werkzeug.utils import secure_filename
from app.resources.general_crud import create

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates'
                            )


# server:port/blueprint_prefix/add
@posts_blueprint.route('/', methods=['GET', 'POST'])
def list_posts():
    user = None
    form_post = PostForm()
    all_posts = PostsModel.query.all()
    authors = UserModel

    try:
        if session['username']:
            user = UserModel.query.filter_by(username=session['username']).first()
            if request.method == 'POST':
                if form_post.text.data is None and form_post.media.data is None:
                    pass
                else:
                    text = form_post.text.data
                    media = form_post.media.data
                    time = datetime.now()
                    print(33)
                    if media:
                        print(35)
                        media_title = secure_filename(f'{user.username}_{media.filename}')
                        print(37)
                        media.save(f'app/static/uploads/post_uploads/{media_title}')
                        print(39)
                    else:
                        print(41)
                        media_title = None
                    print(43)
                    received_data = (time, text, media_title, user.id)
                    print(45)
                    create(received_data, PostsModel)
                    print(47)
                    return redirect('/posts')
    except:
        pass

    return render_template('posts.html', pages=pages_nav_list, user=user, form=form_post, all_posts=all_posts, authors=authors)
