from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class AlbumAwards(Base):
    __tablename__ = "album_awards"

    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)
    award_id = Column(String(50), ForeignKey("award.id"), primary_key=True)

    album = relationship("Album", backref="album_awards")
    award = relationship("Award", backref="album_awards")
