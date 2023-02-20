from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.album.schemas import AlbumSchema
from app.award.schemas import AwardSchema


class AlbumAwardsSchema(BaseModel):
    album_id = UUID4
    award_id = UUID4

    album = AlbumSchema
    award = AwardSchema


album_awards: Optional[List[AlbumAwardsSchema]] = []
