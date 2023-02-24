from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.artist.schemas import ArtistSchema
from app.genre.schemas import GenreSchema


class ArtistGenresSchema(BaseModel):
    artist_id = UUID4
    genre_name = str

    artist = ArtistSchema
    genre = GenreSchema


artist_genres: Optional[List[ArtistGenresSchema]] = []
