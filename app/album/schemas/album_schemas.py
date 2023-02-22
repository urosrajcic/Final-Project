from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator
from pydantic.datetime_parse import date


class AlbumSchema(BaseModel):
    id: UUID4
    name: str
    length: int
    date_of_release: date
    items_sold: Optional[int]
    ratings: Optional[float]
    explicit: Optional[bool]
    lp: Optional[bool]
    ep: Optional[bool]
    single: Optional[bool]
    mixtape: Optional[bool]

    artists: list = []
    songs: dict = {}
    comments: list = []
    awards: list = []
    genres: list = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class AlbumSchemaIn(BaseModel):
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
