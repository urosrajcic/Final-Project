from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.album.schemas import AlbumSchema


class GroupAlbumAssociationSchema(BaseModel):
    group_id = UUID4
    album_id = UUID4

    group = GroupSchema
    album = AlbumSchema


group_album_association: Optional[List[GroupAlbumAssociationSchema]] = []
