from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.artist.schemas import ArtistSchema
from app.album.schemas import AlbumSchema


class ArtistAlbumAssociationSchema(BaseModel):
    artist_id = UUID4
    album_id = UUID4

    artist = ArtistSchema
    album = AlbumSchema


artist_album_association: Optional[List[ArtistAlbumAssociationSchema]] = []
