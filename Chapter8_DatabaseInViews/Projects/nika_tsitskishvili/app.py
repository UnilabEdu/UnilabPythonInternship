from flask import Flask, render_template
from forms import FilterTable, FilterT
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
project_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "wekjfjfj"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#routes
@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/create",methods=['GET','POST'])
def create():
    myform = FilterTable()
    mform = FilterT()
    table_name = None
    if mform.validate_on_submit():
        table_name = mform.table_name.data
        if table_name == "writers" and myform.validate_on_submit():
            name = myform.name.data
            print(name)
            writer = Writer(name)
            db.session.add(writer)
            db.session.commit()


        elif table_name == "novels" and myform.validate_on_submit():

            id = myform.id.data
            name = myform.name.data
            novel = Novel(name,id)
            db.session.add(novel)
            db.session.commit()

        elif table_name == "readers" and myform.validate_on_submit():

            name = myform.name.data
            reader = Reader(name)
            db.session.add(reader)
            db.session.commit()
        else:
            pass
    return render_template("create.html", table_name=table_name, mform=mform, form=myform)

@app.route("/read",methods=['GET','POST'])
def read():
    myform = FilterTable()
    data = None
    author = None
    table_name = None
    if myform.validate_on_submit():
        table_name = myform.table_name.data
        if table_name == "writers":
            name = myform.name.data
            data = Writer.query.filter_by(name=name).first()

        elif table_name == "novels":
            name = myform.name.data
            data = Novel.query.filter_by(name=name).first()
            author = Writer.query.filter_by(id=data.writer_id).first()

        elif table_name == "readers":
            name = myform.name.data
            data = Reader.query.filter_by(name=name).first()

        else:
            pass

    return render_template("read.html", table_name=table_name, author=author, data=data, form=myform)


@app.route("/update",methods=['GET','POST'])
def update():
    myform = FilterTable()
    if myform.validate_on_submit():
        table_name = myform.table_name.data
        name = myform.name.data
        new_name = myform.new_name.data
        if table_name in ["writers","readers","novels"]:
            if table_name == "writers":
                ob = Writer.query.filter_by(name=name).first()
            elif table_name == "novels":
                ob = Novel.query.filter_by(name=name).first()
                if ob != None:
                    new_id = myform.new_id.data
                    ob.writer_id = new_id
            elif table_name == "readers":
                ob = Reader.query.filter_by(name=name).first()
            if ob != None:
                ob.name = new_name
                db.session.commit()


        else:
            pass
    return render_template("update.html", form=myform)

@app.route("/delete",methods=['GET','POST'])
def delete():
    myform = FilterTable()
    if myform.validate_on_submit():
        table_name = myform.table_name.data
        name = myform.name.data
        if table_name != "writers" and table_name != "novels" and table_name != "readers":
            pass
        else:
            if table_name == "writers":
                ob = Writer.query.filter_by(name=name).first()
            elif table_name == "novels":
                ob = Novel.query.filter_by(name=name).first()
            elif table_name == "readers":
                ob = Reader.query.filter_by(name=name).first()
            if ob != None:
                db.session.delete(ob)
                db.session.commit()



    return render_template("delete.html", form=myform)

#models
#crud
# class crud():
#     def create(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self,key,value)
#             self.save()
#     @classmethod
#     def read(cls, name):
#         cls.query.filter_by(name=name).first()
#         #cls.query.filter(cls.age >= 2)
#
#     def update(self,commit=None, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self,key,value)
#         if commit is not None:
#             self.save()
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#     def save(self):
#         db.session.commit(self)
#         db.session.add()

class Writer(db.Model):
    __tablename__ = "writers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    novels = db.relationship("Novel", backref="writer", lazy="dynamic")
    def __init__(self, name):
        self.name = name
    def works(self):
        print("მწერლის ნამუშევრები:")
        for novel in self.novels:
            print(novel.name)
    def __repr__(self):
        return self.name



class Novel(db.Model):
    __tablename__ = "novels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'), nullable=False)
    def __init__(self, name,writer_id):
        self.name = name
        self.writer_id = writer_id

    def __repr__(self):
        return self.name


class Reader(db.Model):
    __tablename__ = "readers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class ReaderNovel(db.Model,):
    __tablename__ = "reader_novel"
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('readers.id'), nullable=False)
    novel_id = db.Column(db.Integer, db.ForeignKey('novels.id'), nullable=False)
    def __init__(self,reader_id,novel_id):
        self.reader_id = reader_id
        self.novel_id = novel_id


if __name__ == "__main__":
    app.run()