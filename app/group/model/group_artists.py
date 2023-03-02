from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupArtists(Base):
    __tablename__ = "group_artists"

    group_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    artist_id = Column(String(50), ForeignKey("artist.id"), primary_key=True)

    group = relationship("Group", backref="group_artists")
    artist = relationship("Artist", backref="group_artists")
