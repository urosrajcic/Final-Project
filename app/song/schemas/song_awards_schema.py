from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.song.schemas import SongSchema
from app.award.schemas import AwardSchema


class SongAwardsSchema(BaseModel):
    song_id = UUID4
    award_id = UUID4

    song = SongSchema
    award = AwardSchema


song_awards: Optional[List[SongAwardsSchema]] = []
