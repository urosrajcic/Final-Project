from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class SongAwards(Base):
    __tablename__ = "song_awards"

    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)
    award_id = Column(String(50), ForeignKey("award.id"), primary_key=True)

    song = relationship("Song", backref="song_awards")
    award = relationship("Award", backref="song_awards")
