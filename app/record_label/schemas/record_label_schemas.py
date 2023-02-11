from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class RecordLabelSchemas(BaseModel):
    id: UUID4
    name: str
    address: str
    date_founded: date
    ratings: float
    biography: str

    country_name: str
    ceo_id: UUID4

    class Config:
        orm_mode = True


class RecordLabelSchemasIn(BaseModel):
    name: str
    address: str
    date_founded: date

    country_name: str
    ceo_id: UUID4

    class Config:
        orm_mode = True
