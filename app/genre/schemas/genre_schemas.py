from pydantic import BaseModel


class GenreSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
