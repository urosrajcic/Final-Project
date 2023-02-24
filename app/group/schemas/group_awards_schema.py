from typing import Optional, List

from pydantic import BaseModel, UUID4

from app.artist.schemas import ArtistSchema
from app.award.schemas import AwardSchema


class ArtistAwardsSchema(BaseModel):
    artist_id = UUID4
    award_id = UUID4

    artist = ArtistSchema
    award = AwardSchema


artist_awards: Optional[List[ArtistAwardsSchema]] = []
