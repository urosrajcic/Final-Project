from pydantic import BaseModel, UUID4, EmailStr
from pydantic.datetime_parse import date

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.country.schemas import CountrySchema
from app.song.schemas import SongSchema


class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    name: str
    surname: str
    date_of_birth: date
    critic: bool
    writer: bool

    country_name: str
    country: CountrySchema
    song_id: UUID4
    song: SongSchema
    artist_id: UUID4
    artist: ArtistSchema
    album_id: UUID4
    album: AlbumSchema

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    name: str
    surname: str
    date_of_birth: date

    country_name: str

    class Config:
        orm_mode = True
