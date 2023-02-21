from datetime import datetime

from pydantic import BaseModel, EmailStr, validator
from pydantic.datetime_parse import date


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    name: str
    surname: str
    date_of_birth: date
    critic: bool
    writer: bool

    country_name: str

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    username: str
    email: str
    password: str
    name: str
    surname: str
    date_of_birth: str
    country_name: str

    @validator('date_of_birth')
    def parse_date(cls, v):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    class Config:
        orm_mode = True
