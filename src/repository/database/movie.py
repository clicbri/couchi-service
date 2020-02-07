from datetime import timedelta, date
from uuid import UUID

from pony.orm.core import PrimaryKey, Required, Set, Optional
from pony.orm.ormtypes import datetime

from .base import db


class Movie(db.Entity):
    _table_ = 'movie'
    id = PrimaryKey(UUID, auto=True)
    title = Required(str)
    year = Required(date)
    synopsis = Required(str)
    duration = Optional(timedelta)
    genres = Optional(str)
    created_at = Required(datetime, default=lambda: datetime.utcnow())
    updated_at = Required(datetime, default=lambda: datetime.utcnow())
    valorations = Set('Valoration')
