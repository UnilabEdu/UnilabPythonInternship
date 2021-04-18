from app import app
from routes import list_pages, list_people, list_posts, auth, success_register, profile, logoff
from flask import session

app.config['SECRET_KEY'] = b"safiiasmfmiq2o4182u9ejdqwr89214y"

if __name__ == '__main__':
    app.run(port=5080, debug=True)
