from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from src.models.product import Product


class ProductApi(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price", type=int,
                        required=True,
                        help="Price is a required parameter and it must be an integer")
    parser.add_argument("name", type=str)
    parser.add_argument("category_id", type=int)

    @jwt_required()
    def get(self):
        get_parser = reqparse.RequestParser()
        get_parser.add_argument("category_id", help="Category id is required", location="args")
        parser = get_parser.parse_args()

        products = Product.query
        if parser["category_id"]:
            products = products.filter_by(category_id=parser["category_id"])

        products = products.all()
        product_json = []
        for product in products:
            product_info = {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "category_id": product.category.id
            }
            product_json.append(product_info)

        return product_json, 200

    def post(self):
        new_parser = self.parser
        parser = new_parser.parse_args()
        new_product = Product(name=parser["name"], price=parser["price"], category_id=parser["category_id"])

        if parser["name"] == "Core i9":
            return "This name is already taken", 400

        new_product.create()
        return new_product.id, 200

    def put(self, id):
        parser = self.parser.parse_args()
        chosen_product = Product.query.get(id)

        if not chosen_product: return "Product with this id was not found", 404

        chosen_product.name = parser["name"]
        chosen_product.price = parser["price"]
        chosen_product.category_id = parser["category_id"]
        chosen_product.save()
        return "Success", 200

    def delete(self, id):
        chosen_product = Product.query.get(id)
        if chosen_product:
            chosen_product.delete()
            return "Success", 200
        else:
            return "Product not found", 404