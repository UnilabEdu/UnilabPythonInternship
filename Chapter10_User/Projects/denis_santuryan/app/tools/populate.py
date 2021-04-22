from app.tools.general_crud import create, update
from app.tools.dummy_data import users
from app.models import UserModel, PostsModel

# populate db with data from data.dummy_data

create(users, UserModel)
