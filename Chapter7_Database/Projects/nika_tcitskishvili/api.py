from app import app
from flask_restful import Resource, Api, marshal_with
from model import SubjectModel
from resoursepars import resource_subject
api = Api(app)
class Subject(Resource):
    @marshal_with(resource_subject)
    def get(self, id):
        if id == 999:
            return SubjectModel.query.all()

