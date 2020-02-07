from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Valoration:
    id: UUID
    movie_id: UUID
    user_id: UUID

    score: int
    is_favorite: bool
    seen: bool
    comment: str

    created_at: datetime
    edited_at: datetime
