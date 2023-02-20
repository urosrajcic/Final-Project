from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.artist.schemas import ArtistSchema
from app.song.schemas import SongSchema


class ArtistSongAssociationSchema(BaseModel):
    artist_id = UUID4
    song_id = UUID4

    artist = ArtistSchema
    song = SongSchema


artist_song_association: Optional[List[ArtistSongAssociationSchema]] = []
