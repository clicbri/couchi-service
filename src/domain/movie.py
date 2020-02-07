from dataclasses import dataclass
from datetime import date, datetime, timedelta
from uuid import UUID


@dataclass
class Movie:
    id: UUID

    title: str
    year: date
    synopsis: str
    duration: timedelta
    genres: list[str]
    verified: bool

    created_at: datetime
    edited_at: datetime
