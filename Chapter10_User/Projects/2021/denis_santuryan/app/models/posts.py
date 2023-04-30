from app import db


class PostsModel(db.Model):
    """
    contains posts' data submitted by users
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    text = db.Column(db.String)
    media = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, time, text=None, media=None, user_id=None):
        self.time = time
        self.text = text
        self.media = media
        self.user_id = user_id

    def __repr__(self):
        return f'ID: {self.id}. {self.media}'

    @classmethod
    def add(cls, time, text, media, user_id):
        post = cls(time, text, media, user_id)
        db.session.add(post)
        db.session.commit()

    # needs an update function
