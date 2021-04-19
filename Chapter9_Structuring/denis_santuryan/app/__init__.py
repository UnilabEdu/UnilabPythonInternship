import os
from flask import Flask  # may need render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# may need these: from routes import list_pages, list_people, list_posts, auth, success_register, profile, logoff from flask import session
# because they were needed in the previous run.py

app = Flask(__name__)

app.config['SECRET_KEY'] = b"safiiasmfmiq2o4182u9ejdqwr89214y"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)


from app.posts.views import posts_blueprint
from app.profiles.views import profiles_blueprint
app.register_blueprint(posts_blueprint, url_prefix="/posts")
app.register_blueprint(profiles_blueprint, url_prefix="/people")


app.add_url_rule('/uploads/<path:filename>',
                 endpoint='uploads',
                 view_func=app.send_static_file)
app.add_url_rule('/people/<path:filename>',
                 endpoint='people',
                 view_func=app.send_static_file)
