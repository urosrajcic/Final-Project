from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.comment.schemas import CommentSchema


class GroupCommentsSchema(BaseModel):
    group_id = UUID4
    comment_id = UUID4

    group = GroupSchema
    comment = CommentSchema


group_comments: Optional[List[GroupCommentsSchema]] = []
