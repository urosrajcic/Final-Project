from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.song.schemas import SongSchema
from app.comment.schemas import CommentSchema


class SongCommentsSchema(BaseModel):
    song_id = UUID4
    comment_id = UUID4

    song = SongSchema
    comment = CommentSchema


song_comments: Optional[List[SongCommentsSchema]] = []
