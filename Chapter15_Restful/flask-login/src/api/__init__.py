from flask_restful import Api
from src.api.product import ProductApi


api = Api()
api.add_resource(ProductApi, "/product", "/product/<int:id>")