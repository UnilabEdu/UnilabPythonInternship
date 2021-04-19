# მეგონა ეგეთი სტრუქტურით იმუშავებდა მაგრამ მოდელების დატოვება მომიწია app.py-ში
# რადგან 'flask db migrate'-ს შემდეგ ყველა table იშლებოდა
#
#
#
#
#
#
#
# from app import db
#
#
# class UserModel(db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     full_name = db.Column(db.String)
#     email = db.Column(db.String)
#     age = db.Column(db.Integer)
#     sex = db.Column(db.String)
#     phone = db.Column(db.String)
#
#     def __init__(self, username, full_name, email, age, sex, phone):
#         self.username = username
#         self.full_name = full_name
#         self.email = email
#         self.age = age
#         self.sex = sex
#         self.phone = phone
#
#     def __repr__(self):
#         return f'{self.username}: {self.full_name}, {self.sex}, aged {self.age}. Contact: {self.email, self.phone}'
#
#
# class PagesModel(db.Model):
#     __tablename__ = 'pages'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     followers = db.Column(db.Integer)
#     topic = db.Column(db.String)
#
#     def __init__(self, title, followers, topic):
#         self.title = title
#         self.followers = followers
#         self.topic = topic
#
#     def __repr__(self):
#         return f'{self.title} with {self.followers} followers. Topic: {self.topic}'
