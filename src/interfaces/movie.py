from abc import ABC, abstractmethod
from ..domain.movie import Movie as MovieDomain


class Movie(ABC):
    @staticmethod
    @abstractmethod
    def save(movie: MovieDomain):
        pass

    @staticmethod
    @abstractmethod
    def get(movie_id: str) -> MovieDomain:
        pass
