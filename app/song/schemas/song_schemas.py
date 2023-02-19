from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, UUID4, validator
from pydantic.datetime_parse import date

from app.artist import Artist
from app.award.schemas import AwardSchema
from app.genre.schemas import GenreSchema


class SongSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    date_of_release: date
    items_sold: Optional[int] = None
    lyrics: Optional[str] = None
    ratings: Optional[float] = None
    explicit: Optional[bool] = False
    genre_name: Optional[str] = None
    award_id: Optional[str] = None

    genre: GenreSchema
    award: AwardSchema

    artists: Optional[List[Artist]] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class SongSchemaIn(BaseModel):
    name: str
    length: int
    date_of_release: str

    @validator('date_of_release')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
