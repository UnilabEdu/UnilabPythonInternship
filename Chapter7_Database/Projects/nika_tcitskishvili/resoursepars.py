from flask_restful import reqparse, fields
resource_subject = {
    "id": fields.Integer,
    "title": fields.String,
    "students": fields.String,
    "teacher": fields.String
}

resource_teacher = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "subject_id": fields.Integer
}
resource_student = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "subject_id": fields.Integer
}
subjectparser = reqparse.RequestParser()
subjectparser.add_argument("id", type=int, help='Id must be integer')
subjectparser.add_argument("title", type=str, help='Title must be string')
subjectparser.add_argument("students", type=list, help='Students must be list')
subjectparser.add_argument("teacher", type=str, help='Teacher must be string')

teacherparser = reqparse.RequestParser()
teacherparser.add_argument("id", type=int, help='Id must be integer')
teacherparser.add_argument("first_name", type=str, help='First name must be string')
teacherparser.add_argument("last_name", type=str, help='Last name must be string')
teacherparser.add_argument("subject_id", type=int, help='Subject_id must be integer')

studentparser = reqparse.RequestParser()
studentparser.add_argument("id", type=int, help='Id must be integer')
studentparser.add_argument("first_name", type=str, help='First name must be string')
studentparser.add_argument("last_name", type=str, help='Last name must be string')
studentparser.add_argument("subject_id", type=int, help='Subject_id must be integer')