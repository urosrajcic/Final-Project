from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import datetime


class CommentSchemas(BaseModel):
    id: UUID4
    header: str
    text: str
    datetime: datetime
    ratings: float

    user_username: str
    song_id: UUID4
    artist_id: UUID4
    album_id: UUID4
    record_label_id: UUID4

    class Config:
        orm_mode = True


class CommentSchemasIn(BaseModel):
    header: str
    text: str
    datetime: datetime
    ratings: float

    user_username: str

    class Config:
        orm_mode = True
