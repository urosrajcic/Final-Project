from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class AwardSchema(BaseModel):
    name: str
    award_date: date

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    name: str
    award_date: date

    class Config:
        orm_mode = True
