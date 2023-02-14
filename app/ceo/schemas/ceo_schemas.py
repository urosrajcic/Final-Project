from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class CEOSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    date_of_birth: date
    from_date: date
    too_date: date
    active: bool

    class Config:
        orm_mode = True


class CEOSchemaIn(BaseModel):
    name: str
    surname: str
    date_of_birth: date
    from_date: date

    class Config:
        orm_mode = True
