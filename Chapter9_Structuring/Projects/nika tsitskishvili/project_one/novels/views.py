from project_one.novels.models import Novel
from flask import render_template, Blueprint
from project_one.novels.forms import FilterTable
from project_one.writers.models import Writer
novels_blueprint = Blueprint('novels', __name__, static_folder='static', template_folder='templates')


@novels_blueprint.route("/create", methods=["GET","POST"])
def create():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        id = myform.id.data
        Novel.create(name=name, writer_id=id)
    else:
        pass
    return render_template("create.html", myform=myform)

@novels_blueprint.route("/read", methods=["GET","POST"])
def read():
    myform = FilterTable()
    data, author = None, None
    name = myform.name.data
    if myform.validate_on_submit() and myform.submit.data:
        data = Novel.read(name=name)
        author = Writer.query.filter_by(id=Novel.query.filter_by(name=name).first().writer_id).first().name
    else:
        pass
    return render_template("read.html", author=author, data=data, myform=myform)


@novels_blueprint.route("/update", methods=["GET","POST"])
def update():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        new_name = myform.new_name.data
        new_id = myform.new_id.data
        Novel.update(name=name, new_name=new_name, new_id=new_id)
    else:
        pass
    return render_template("update.html", myform=myform)

@novels_blueprint.route("/delete", methods=["GET","POST"])
def delete():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        Novel.delete(name)
    return render_template("delete.html", myform=myform)
