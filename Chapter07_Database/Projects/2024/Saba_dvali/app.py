from src import create_app

from src.models.base import BaseModel
from src.models.images import Images
from src.models.user import Users
from src.models.product import Products
from src.models.role import Role
from src.ext import db

flask_app = create_app()

if __name__ == "__main__":
    with flask_app.app_context():
        db.create_all()
    flask_app.run(debug=True, host="0.0.0.0", port=8080)