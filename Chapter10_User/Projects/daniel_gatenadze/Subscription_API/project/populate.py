from .user.models import User, Role, UserRoles
from .subscription_plans.models import SubsPlan
from .extensions import db
from .project import create_app
from werkzeug.security import generate_password_hash

application = create_app()
application.app_context().push()
#
#
# # Database File #
# db.drop_all()
db.create_all()


def my_function():
    with application.app_context():
        user1 = User(username='usename1', email='user@user.com', password=generate_password_hash('password123', method='sha256'), gender="Male", age='32',)
        user2 = User(username='usename2', email='user2@user.com', password=generate_password_hash('password123', method='sha256'), gender="Femboy", age='22',)
        subsplan = SubsPlan('basic', 6.99)
        subsplan2 = SubsPlan('Average', 14.99)
        subsplan3 = SubsPlan('Premium', 30.00)
        role1 = Role(name='user')
        role2 = Role(name='admin')
        db.session.add_all([subsplan, subsplan2, subsplan3])
        db.session.add_all([role1, role2])
        db.session.flush()
        db.session.add_all([user1, user2])
        db.session.commit()
        user_role1 = UserRoles(user_id=user1.id, role_id=role1.id)
        user_role2 = UserRoles(user_id=user2.id, role_id=role2.id)
        db.session.add_all([user_role1, user_role2])
        db.session.commit()


#

# my_function()
