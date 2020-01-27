from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class User:
    id: UUID
    nick: str

    createdAt: datetime
    editedAt: datetime