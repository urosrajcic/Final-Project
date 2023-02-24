from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class ArtistSchema(BaseModel):
    id: UUID4
    name: str
    date_of_birth: Optional[date]
    date_of_death: Optional[date]
    ratings: Optional[float]
    vocalist: Optional[bool]
    musician: Optional[bool]
    producer: Optional[bool]
    writer: Optional[bool]
    engineer: Optional[bool]
    biography: Optional[str]
    country_name: str
    record_label_id: Optional[UUID4]

    songs = []
    albums = []
    comments = []
    awards = []
    genres = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ArtistSchemaIn(BaseModel):
    name: str
    country_name: str
    date_of_birth: Optional[str]
    date_of_death: Optional[str]
    vocalist: Optional[bool]
    musician: Optional[bool]
    producer: Optional[bool]
    writer: Optional[bool]
    engineer: Optional[bool]
    biography: Optional[str]
    record_label_id: Optional[UUID4]

    @validator('date_of_birth')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ArtistSchemaOut(BaseModel):
    id: UUID4
    name: str
    date_of_birth: Optional[date]
    date_of_death: Optional[date]
    ratings: Optional[float]
    vocalist: Optional[bool]
    musician: Optional[bool]
    producer: Optional[bool]
    writer: Optional[bool]
    engineer: Optional[bool]
    biography: Optional[str]
    country_name: str
    record_label_id: Optional[UUID4]
    genres: list = []

    class Config:
        orm_mode = True
