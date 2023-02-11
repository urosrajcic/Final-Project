from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class UserSchemas(BaseModel):
    username: str
    email: str
    password: str
    name: str
    surname: str
    date_of_birth: date
    critic: bool
    writer: bool

    country_name: str
    song_id: UUID4
    artist_id: UUID4
    album_id: UUID4

    class Config:
        orm_mode = True


class UserSchemasIn(BaseModel):
    username: str
    email: str
    password: str
    name: str
    surname: str
    date_of_birth: date
    critic: bool
    writer: bool

    country_name: str

    class Config:
        orm_mode = True
