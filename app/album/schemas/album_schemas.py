from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


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
    artist_id: UUID4
    genre_name: str
    award_name: str
    user_username: str
    record_label_id: UUID4

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
