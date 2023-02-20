from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.artist.schemas import ArtistSchema
from app.comment.schemas import CommentSchema


class ArtistCommentsSchema(BaseModel):
    artist_id = UUID4
    comment_id = UUID4

    artist = ArtistSchema
    comment = CommentSchema


artist_comments: Optional[List[ArtistCommentsSchema]] = []
