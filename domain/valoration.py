from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Valoration:
    id: UUID
    movieId: UUID
    userId: UUID

    score: int
    isFavorite: bool
    seen: bool
    comment: str

    createdAt: datetime
    editedAt: datetime