from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.record_label.schemas import RecordLabelSchema
from app.song.schemas import SongSchema
from app.user.schemas import UserSchema


class CommentSchema(BaseModel):
    id: UUID4
    header: str
    text: str
    date_time: datetime
    ratings: Optional[float]

    user_username: str
    user: UserSchema
    song_id: Optional[UUID4]
    song: SongSchema
    artist_id: Optional[UUID4]
    artist: ArtistSchema
    album_id: Optional[UUID4]
    album: AlbumSchema
    record_label_id: Optional[UUID4]
    record_label: RecordLabelSchema

    class Config:
        orm_mode = True


class CommentSchemaIn(BaseModel):
    header: str
    text: str
    date_time: datetime
    user_username: str

    class Config:
        orm_mode = True
