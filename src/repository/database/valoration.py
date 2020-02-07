from pony.orm.core import PrimaryKey, Required, Optional
from pony.orm.ormtypes import datetime

from src.repository.database.movie import Movie
from src.repository.database.user import User
from .base import db


class Valoration(db.Entity):
    users = Required(User)
    movies = Required(Movie)
    score = Optional(int)
    is_favorite = Optional(bool)
    seen = Optional(bool)
    comment = Optional(str)
    created_at = Optional(datetime, default=lambda: datetime.utcnow())
    updated_at = Optional(datetime, default=lambda: datetime.utcnow())
    PrimaryKey(users, movies)
