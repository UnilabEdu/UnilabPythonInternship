from general_crud import create, update
from resources.resources import users, pages_resource
from app import UserModel, PagesModel

# populate db with data from resources.resources

create(users, UserModel)
create(pages_resource, PagesModel)


# create a one-to-one relationship between users and pages
