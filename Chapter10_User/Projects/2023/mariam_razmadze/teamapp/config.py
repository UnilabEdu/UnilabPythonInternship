import os

class Config(object):
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY='sjhdajskdjhajskdhiuheiuy871y27831632817326812738hekhfksjfhksdf'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    #postgres://mariam:wnHJal0QQ8oeCyuSKjW9bXf2KudlGcLW@dpg-cf5bhepa6gdq37n1dib0-a.frankfurt-postgres.render.com/factorypattern
    FLASK_ADMIN_SWATCH='united'