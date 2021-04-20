from app.resources.general_crud import create, update
from app.resources.dummy_data import users
from app.models import UserModel, PostsModel

# populate db with data from resources.resources

create(users, UserModel)
# create(, PostsModel)
