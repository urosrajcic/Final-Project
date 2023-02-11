from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date


class AwardSchema(BaseModel):
    name: str
    award_date: date

    song_id: UUID4
    artist_id: UUID4
    album_id: UUID4

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
