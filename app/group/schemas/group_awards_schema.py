from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.group.schemas import GroupSchema
from app.award.schemas import AwardSchema


class GroupAwardsSchema(BaseModel):
    group_id = UUID4
    award_id = UUID4

    group = GroupSchema
    award = AwardSchema


group_awards: Optional[List[GroupAwardsSchema]] = []
