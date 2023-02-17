from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date
from app.album.schemas import AlbumSchema
from app.award.schemas import AwardSchema
from app.country.schemas import CountrySchema
from app.genre import GenreSchema
from app.record_label.schemas import RecordLabelSchema
from app.song.schemas import SongSchema
from app.user.schemas import UserSchema


class ArtistSchema(BaseModel):
    id: UUID4
    name: str
    date_of_birth: date
    date_of_death: date
    ratings: float
    vocalist: bool
    musician: bool
    producer: bool
    writer: bool
    engineer: bool
    biography: str

    album_id: UUID4
    album: AlbumSchema
    song_id: UUID4
    song: SongSchema
    genre_name: str
    genre: GenreSchema
    award_name: str
    award: AwardSchema
    country_name: str
    country: CountrySchema
    user_username: str
    user: UserSchema
    record_label_id: UUID4
    record_label: RecordLabelSchema

    class Config:
        orm_mode = True


class ArtistSchemaIn(BaseModel):
    name: str
    date_of_birth: date

    country_name: str

    class Config:
        orm_mode = True
