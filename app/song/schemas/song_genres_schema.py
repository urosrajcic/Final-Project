from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.song.schemas import SongSchema
from app.genre.schemas import GenreSchema


class SongGenresSchema(BaseModel):
    song_id = UUID4
    genre_name = str

    song = SongSchema
    genre = GenreSchema


song_genres: Optional[List[SongGenresSchema]] = []
