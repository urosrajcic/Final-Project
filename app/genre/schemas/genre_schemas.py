from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.song.schemas import SongSchema


class GenreSchema(BaseModel):
    name: str

    song_id: UUID4
    song: SongSchema
    artist_id: UUID4
    artist: ArtistSchema
    album_id: UUID4
    album: AlbumSchema

    class Config:
        orm_mode = True


class GenreSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
