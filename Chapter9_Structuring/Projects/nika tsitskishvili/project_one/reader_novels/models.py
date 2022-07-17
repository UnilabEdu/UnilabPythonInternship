from project_one.extensions import db
class ReaderNovel(db.Model,):
    __tablename__ = "reader_novel"
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('readers.id'), nullable=False)
    novel_id = db.Column(db.Integer, db.ForeignKey('novels.id'), nullable=False)
    def __init__(self,reader_id,novel_id):
        self.reader_id = reader_id
        self.novel_id = novel_id