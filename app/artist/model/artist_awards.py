from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class ArtistAwards(Base):
    __tablename__ = "artist_awards"

    artist_id = Column(String(50), ForeignKey("artist.id"), primary_key=True)
    award_id = Column(String(50), ForeignKey("award.id"), primary_key=True)

    artist = relationship("Artist", backref="artist_award")
    award = relationship("Award", backref="artist_award")
