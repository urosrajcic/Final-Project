from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.song.schemas import SongSchema


class AlbumSongAssociationSchema(BaseModel):
    album_id = UUID4
    song_id = UUID4

    album = AlbumSchema
    song = SongSchema


album_song_association: Optional[List[AlbumSongAssociationSchema]] = []
