from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4, validator
from pydantic.datetime_parse import date

from app.country.schemas import CountrySchema


class RecordLabelSchema(BaseModel):
    id: UUID4
    name: str
    address: str
    date_founded: date
    ceo: str

    country_name: str
    country: CountrySchema

    ratings: Optional[float]
    biography: Optional[str]

    class Config:
        orm_mode = True


class RecordLabelSchemaIn(BaseModel):
    name: str
    address: str
    date_founded: str
    ceo: str

    country_name: str

    @validator('date_founded')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
