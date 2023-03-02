from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.artist.schemas import ArtistSchema


class GroupArtistsSchema(BaseModel):
    group_id = UUID4
    artist_id = UUID4

    group = GroupSchema
    artist = ArtistSchema


group_artists: Optional[List[GroupArtistsSchema]] = []
