from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class SongSchemas(BaseModel):
    id: UUID4
    name: str
    length: int
    items_sold: int
    lyrics: str
    date_of_release: date
    ratings: float
    explicit: bool

    album_id: UUID4
    artist_id: UUID4
    genre_name: str
    award_name: str
    user_username: str
    record_label_id: UUID4

    class Config:
        orm_mode = True


class SongSchemasIn(BaseModel):
    name: str
    length: int
    items_sold: int
    lyrics: str
    date_of_release: date
    ratings: float
    explicit: bool

    genre_name: str
    award_name: str
    user_username: str

    class Config:
        orm_mode = True
