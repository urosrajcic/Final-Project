from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.country.schemas import CountrySchema


class RecordLabelSchema(BaseModel):
    id: UUID4
    name: str
    address: str
    date_founded: date
    ratings: float
    biography: str
    ceo: str

    country_name: str
    country: CountrySchema

    class Config:
        orm_mode = True


class RecordLabelSchemaIn(BaseModel):
    name: str
    address: str
    date_founded: str
    ratings: float
    biography: str
    ceo: str

    country_name: str

    class Config:
        orm_mode = True
