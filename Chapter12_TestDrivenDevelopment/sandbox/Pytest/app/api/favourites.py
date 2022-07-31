from flask_restful import Resource, reqparse
from app.models.user import User
from app.models.movie import Movie
from app.ext import db


class FavouritesApi(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'key',
        type=str,
        required=True,
        nullable=False)

    parser.add_argument(
        'movie_id',
        type=int,
        required=True,
        nullable=False)

    def post(self):

        received_arguments = self.parser.parse_args()

        user = User.query.filter_by(developer_key=received_arguments['key']).first()
        movie = Movie.query.get(received_arguments['movie_id'])

        if not user:
            return 404

        if not movie:
            return 404

        user.favourite_movies.append(movie)
        db.session.commit()

        return 200

    def post(self):

        received_arguments = self.parser.parse_args()

        user = User.query.filter_by(developer_key=received_arguments['key']).first()
        movie = Movie.query.get(received_arguments['movie_id'])

        if not user:
            return "Not Found", 404

        if not movie:
            return "Not Found", 404

        user.favourite_movies.append(movie)
        db.session.commit()

        return 200


