from data import writer_data,novel_data,reader_data, reader_novel_data
from app import Writer,Novel,Reader,ReaderNovel
from app import db

def create_database():
    for i in writer_data:
        writer = Writer(i["name"])
        db.session.add(writer)
        db.session.commit()
    for j in novel_data:
        novel = Novel(j["name"],j["writer_id"])
        db.session.add(novel)
        db.session.flush()
    for k in reader_data:
        reader = Reader(k["name"])
        db.session.add(reader)
        db.session.commit()
    for x in reader_novel_data:
        reader = ReaderNovel(x["reader_id"],x["novel_id"])
        db.session.add(reader)
        db.session.commit()


#
#
