from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.artist.schemas import ArtistSchema
from app.award.schemas import AwardSchema
from app.genre import GenreSchema
from app.record_label.schemas import RecordLabelSchema
from app.song.schemas import SongSchema
from app.user.schemas import UserSchema


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
    user_username: str
    user: UserSchema
    record_label_id: UUID4
    record_label: RecordLabelSchema

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
