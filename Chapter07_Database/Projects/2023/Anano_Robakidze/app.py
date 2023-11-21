from flask import Flask
import os


app = Flask(__name__, template_folder='template')
app.config["SECRET_KEY"] = "abjdlhrjekls78akkjlllakqawss"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TRACK_DATABASE_MODIFICATIONS"] = False

UPLOAD_PATH = os.path.join(app.root_path, "static", "img")

# product_list = {
#     "Clothes": [
#         {"name": "Shirt", "color": "red", "size": "S", "img": "apparel-162192_1280.png", "price": 100},
#         {"name": "Coat Jacket", "color": "grey", "size": "M", "img": "coat-30208_1280.png", "price": 200}
#     ],
#
#     "Shoes": [
#         {"name": "Shoes", "color": "brown", "size": "M", "img": "clothes-1295223_1280.png", "price": 250}
#     ]
# }




if __name__ == '__main__':
    from routes import *
    app.run(debug=True)