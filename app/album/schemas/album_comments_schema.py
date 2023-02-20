from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.comment.schemas import CommentSchema


class AlbumCommentsSchema(BaseModel):
    album_id = UUID4
    comment_id = UUID4

    album = AlbumSchema
    comment = CommentSchema


album_comments: Optional[List[AlbumCommentsSchema]] = []
