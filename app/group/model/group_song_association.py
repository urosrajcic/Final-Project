from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupSongAssociation(Base):
    __tablename__ = "group_song_association"

    group_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)

    group = relationship("Group", backref="group_song_association")
    song = relationship("Song", backref="group_song_association")
