from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.award.schemas import AwardSchema
from app.genre import GenreSchema
from app.record_label.schemas import RecordLabelSchema
from app.user.schemas import UserSchema


class SongSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    items_sold: int
    lyrics: str
    date_of_release: date
    ratings: float
    explicit: bool

    album_id: UUID4
    album: AlbumSchema
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


class SongSchemaIn(BaseModel):
    name: str
    length: int
    date_of_release: date

    artist_id: UUID4

    class Config:
        orm_mode = True
