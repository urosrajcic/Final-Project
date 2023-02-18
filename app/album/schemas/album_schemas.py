from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.artist.schemas import ArtistSchema
from app.award.schemas import AwardSchema
from app.genre import GenreSchema
from app.song.schemas import SongSchema


class AlbumSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    date_of_release: date
    items_sold: int
    ratings: int
    explicit: bool
    lp: bool
    ep: bool
    single: bool
    mixtape: bool

    song_id: UUID4
    song: SongSchema
    artist_id: UUID4
    artist: ArtistSchema
    genre_name: str
    genre: GenreSchema
    award_name: str
    award: AwardSchema

    class Config:
        orm_mode = True


class AlbumSchemaIn(BaseModel):
    name: str
    length: int
    date_of_release: date
    explicit: bool

    song_id: UUID4
    artist_id: UUID4
    genre_name: str

    class Config:
        orm_mode = True
