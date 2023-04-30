from app import db
from models import User, Type

# db.drop_all()
# db.create_all()
#
# type1 = Type("User")
# type2 = Type("Creator")
# type3 = Type("Venue")
# db.session.add_all([type1, type2, type3])
# db.session.flush()
#
#
# user1 = User("rando", "rando@rando.com", "randopass", "beginner", 1)
# user2 = User("bro", "bro@bro.com", "bropass", "small experience", 2)
# user3 = User("m", "m@m.com", "mpass", "veteran", 2)
# user4 = User("b", "b@b.com", "bpass", "veteran", 3)
# db.session.add_all([user1, user2, user3, user4])
# db.session.commit()

type = Type.query.get(2)
for user in type.users:
    print(user.username)

user = User.query.get(1)
print(user.type.name)
