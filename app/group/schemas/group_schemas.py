from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class GroupSchema(BaseModel):
    id: UUID4
    name: str
    date_of_forming: Optional[date]
    date_of_disband: Optional[date]
    ratings: Optional[float]
    vocalist: Optional[bool]
    musician: Optional[bool]
    producer: Optional[bool]
    writer: Optional[bool]
    engineer: Optional[bool]
    biography: Optional[str]
    country_name: str
    record_label_id: Optional[UUID4]

    artists = []
    songs = []
    albums = []
    comments = []
    awards = []
    genres = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class GroupSchemaIn(BaseModel):
    name: str
    country_name: str
    date_of_forming: Optional[str]
    date_of_disband: Optional[str]
    biography: Optional[str]
    record_label_id: Optional[UUID4]

    @validator('date_of_forming')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class GroupSchemaOut(BaseModel):
    id: UUID4
    name: str
    date_of_forming: Optional[date]
    date_of_disband: Optional[date]
    ratings: Optional[float]
    biography: Optional[str]
    country_name: str
    record_label_id: Optional[UUID4]

    genres: list
    artists: list

    class Config:
        orm_mode = True
