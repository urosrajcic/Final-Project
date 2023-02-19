from pydantic import BaseModel, EmailStr
from pydantic.datetime_parse import date

from app.country.schemas import CountrySchema


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    name: str
    surname: str
    date_of_birth: date
    critic: bool = False
    writer: bool = False

    country_name: str
    country: CountrySchema

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

    class Config:
        orm_mode = True
