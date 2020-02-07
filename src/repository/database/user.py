from uuid import UUID

from pony.orm.core import PrimaryKey, Required, Set
from pony.orm.ormtypes import datetime

from .base import db


class User(db.Entity):
    _table_ = 'user'
    id = PrimaryKey(UUID, auto=True)
    nick = Required(str, unique=True)
    created_at = Required(datetime, default=lambda: datetime.utcnow())
    updated_at = Required(datetime, default=lambda: datetime.utcnow())
    valorations = Set('Valoration')
