from typing import Optional

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
    items_sold: Optional[int] = None
    ratings: Optional[float] = None
    explicit: Optional[bool] = False
    lp: Optional[bool] = False
    ep: Optional[bool] = False
    single: Optional[bool] = False
    mixtape: Optional[bool] = False

    genre_name: Optional[str] = None
    genre: GenreSchema
    award_id: Optional[str] = None
    award: AwardSchema

    class Config:
        orm_mode = True


class AlbumSchemaIn(BaseModel):
    name: str
    length: int
    date_of_release: str

    class Config:
        orm_mode = True
