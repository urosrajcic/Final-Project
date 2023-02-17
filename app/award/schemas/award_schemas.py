from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date

from app.song.schemas import SongSchema
from app.artist.schemas import ArtistSchema
from app.album.schemas import AlbumSchema


class AwardSchema(BaseModel):
    name: str
    award_date: date

    song_id: UUID4
    song: SongSchema
    artist_id: UUID4
    artist: ArtistSchema
    album_id: UUID4
    album: AlbumSchema

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    name: str
    award_date: date

    class Config:
        orm_mode = True
