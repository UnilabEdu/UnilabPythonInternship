# from source.extensions import db
# from source import create_app
# from user.models import User
#
# app = create_app()
# app.app_context().push()
#
# db.drop_all()
# db.create_all()
#
#
# def populate():
#     with app.app_context():
#         test_user = User(username='test',
#                          email='test@email.com',
#                          password='test_pass',
#                          experience='test',
#                          account_type='test')
#         db.session.add(test_user)
#         db.session.commit()
#
#
# populate()
