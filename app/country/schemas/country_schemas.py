from pydantic import BaseModel


class CountrySchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CountrySchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
