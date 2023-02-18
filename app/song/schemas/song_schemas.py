from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.artist.schemas import ArtistSchema
from app.award.schemas import AwardSchema
from app.genre import GenreSchema


class SongSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    items_sold: int
    lyrics: str
    date_of_release: date
    ratings: float
    explicit: bool

    artist_id: UUID4
    artist: ArtistSchema
    genre_name: str
    genre: GenreSchema
    award_name: str
    award: AwardSchema

    class Config:
        orm_mode = True


class SongSchemaIn(BaseModel):
    name: str
    length: int
    date_of_release: date

    artist_id: UUID4

    class Config:
        orm_mode = True
