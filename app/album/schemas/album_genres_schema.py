from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.genre.schemas import GenreSchema


class AlbumGenresSchema(BaseModel):
    album_id = UUID4
    genre_name = str

    album = AlbumSchema
    genre = GenreSchema


album_genres: Optional[List[AlbumGenresSchema]] = []
