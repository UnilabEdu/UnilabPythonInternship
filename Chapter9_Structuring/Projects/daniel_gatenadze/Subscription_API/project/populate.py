from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.users.models import User
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.subscription_plans.models import SubsPlan
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.extensions import db
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project import create_app

app = create_app()
app.app_context().push()
#
#
# # Database File #
#
db.drop_all()
db.create_all(app=create_app())


def my_function():
    with app.app_context():
        user1 = User(username='something', email='ass', password='fk', gender="Male", age='32',)
        user2 = User(username='ber', email='ss', password='rr', gender="Femboy", age='22',)
        user3 = User(username='asd', email='123', password='444', gender="bruh", age='54',)
        subsplan = SubsPlan('basic', 6.99)
        subsplan2 = SubsPlan('Average', 14.99)
        subsplan3 = SubsPlan('Premium', 30.00)
        db.session.add_all([subsplan, subsplan2, subsplan3])
        db.session.flush()
        db.session.add_all([user1, user2, user3])
        db.session.commit()
#

my_function()

