from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator
from pydantic.datetime_parse import date


class SongSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    date_of_release: date
    items_sold: Optional[int]
    lyrics: Optional[str]
    ratings: Optional[float]
    explicit: Optional[bool]

    artists = []
    albums = []
    comments = []
    awards = []
    genres = []

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
