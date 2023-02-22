from datetime import datetime

from pydantic import BaseModel, UUID4, validator
from pydantic.datetime_parse import date


class AwardSchema(BaseModel):
    id: UUID4
    name: str
    category: str
    award_date: date

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    name: str
    category: str
    award_date: str

    @validator('award_date')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
