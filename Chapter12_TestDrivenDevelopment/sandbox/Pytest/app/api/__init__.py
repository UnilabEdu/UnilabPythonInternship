from flask_restful import Api
from app.api.search import SearchApi
from app.api.favourites import FavouritesApi

api = Api(prefix='/api/')
api.add_resource(SearchApi, 'search')
api.add_resource(FavouritesApi, 'favourites')