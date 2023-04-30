from flask_restful import Resource, reqparse
from app.models.movie import Movie


class SearchApi(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'query',
        type=str,
        required=False)

    parser.add_argument(
        'genre',
        type=str,
        required=False)

    def get(self):

        received_arguments = self.parser.parse_args()
        found_movies = Movie.query

        if received_arguments['query']:
            query = received_arguments['query'].lower()
            found_movies = found_movies.filter(Movie.name.ilike("%" + query + "%"))

        if received_arguments['genre']:
            found_movies = found_movies.filter_by(genre=received_arguments['genre'])

        found_movies = found_movies.all()
        found_movies = [{"name": movie.name, "rating": movie.rating, "genre": movie.genre} for movie in found_movies]

        return found_movies


