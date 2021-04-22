from general_crud import create, update
from resources.resources import users
from app import UserModel, PostsModel

# populate db with data from resources.resources

create(users, UserModel)
# create(, PostsModel)
