from project import db, User, SubsPlan

# Database File #
#
# db.drop_all()
# db.create_all()
#
# subsplan = SubsPlan('basic', 6.99)
# subsplan2 = SubsPlan('Average', 14.99)
# subsplan3 = SubsPlan('Premium', 30.00)
#
# # #
# db.session.add_all([subsplan, subsplan2, subsplan3])
# db.session.flush()
# #
# user1 = User(username='something', email='ass', password='fk', gender="Male", age='32', )
# user2 = User(username='ber', email='ss', password='rr', gender="Femboy", age='22', )
# user3 = User(username='asd', email='123', password='444', gender="bruh", age='54', )
#
# db.session.add_all([user1, user2, user3])
# db.session.commit()

# subscription = SubsPlan.query.get(1)
# for subs in subscription.users:
#     print(subs.username)

# subscription = SubsPlan.query.get(1)
# print(subscription.subb.name)
