from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, UUID4, validator

from app.award.schemas import AwardSchema
from app.country.schemas import CountrySchema
from app.genre import GenreSchema
from app.record_label.schemas import RecordLabelSchema
from app.song.schemas import SongSchema


class ArtistSchema(BaseModel):
    id: UUID4
    name: str
    date_of_birth: date
    date_of_death: Optional[date] = None
    ratings: Optional[float] = None
    vocalist: Optional[bool] = False
    musician: Optional[bool] = False
    producer: Optional[bool] = False
    writer: Optional[bool] = False
    engineer: Optional[bool] = False
    biography: Optional[str] = None
    country_name: str
    genre_name: Optional[str] = None
    award_id: Optional[str] = None
    record_label_id: Optional[str] = None

    country: CountrySchema
    genre: GenreSchema
    award: AwardSchema
    record_label: RecordLabelSchema

    songs: Optional[List[SongSchema]] = []

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
