from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# @app.route("/", methods=["GET"])
# def data():
#     data = Subject.query.all()
#     data_dict = {"subjects":
#         [
#             {"title": data[0].title,
#              "teacher": data[0].teacher.first_name + " " + data[0].teacher.last_name,
#              "students": students_names[:4]
#              },
#
#             {"title": data[1].title,
#              "teacher": data[1].teacher.first_name + " " + data[1].teacher.last_name,
#              "students": students_names[4:]
#              },
#         ]
#     }
#     return data_dict
#
#
# # ,methods=["GET", "POST"]
# data_one = Subject.query.all()
# print(data[0].students)
# print(data[1].students)


if __name__ == "__main__":
    app.run(debug=True)
