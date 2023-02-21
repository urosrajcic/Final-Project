from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator

from app.country.schemas import CountrySchema


class ArtistSchema(BaseModel):
    id: UUID4
    name: str
    date_of_birth: date
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
    date_of_birth: str

    @validator('date_of_birth')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
