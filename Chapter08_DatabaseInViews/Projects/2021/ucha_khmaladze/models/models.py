from CRUD.crud import Crud

class UserInfo(db.Model, Crud):

    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    def __repr__(self):

        return f'you have done great {self.name} {self.last_name} your email is {self.email}'