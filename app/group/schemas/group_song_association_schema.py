from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.song.schemas import SongSchema


class GroupSongAssociationSchema(BaseModel):
    group_id = UUID4
    song_id = UUID4

    group = GroupSchema
    song = SongSchema


group_song_association: Optional[List[GroupSongAssociationSchema]] = []
