from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


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
    song_id: UUID4
    genre_name: str
    award_name: str
    country_name: str
    user_username: str
    record_label_id: UUID4

    class Config:
        orm_mode = True


class ArtistSchemaIn(BaseModel):
    name: str
    date_of_birth: date

    country_name: str

    class Config:
        orm_mode = True
