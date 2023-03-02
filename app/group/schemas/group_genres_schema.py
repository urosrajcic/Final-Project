from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.genre.schemas import GenreSchema


class GroupGenresSchema(BaseModel):
    group_id = UUID4
    genre_name = str

    group = GroupSchema
    genre = GenreSchema


group_genres: Optional[List[GroupGenresSchema]] = []
