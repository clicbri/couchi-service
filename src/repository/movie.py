import string

from ..interfaces.movie import Movie as MovieInterface
from ..domain.movie import Movie as MovieDomain


class MovieSQLAdapter(MovieInterface):
    @staticmethod
    def save(movie: MovieDomain):
        pass

    @staticmethod
    def get(movie_id: string) -> MovieDomain:
        pass
