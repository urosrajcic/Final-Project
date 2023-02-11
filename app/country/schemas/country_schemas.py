from pydantic import BaseModel


class CountrySchemas(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CountrySchemasIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
