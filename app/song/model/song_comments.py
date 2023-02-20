from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class SongComments(Base):
    __tablename__ = "song_comments"

    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)
    comment_id = Column(String(50), ForeignKey("comment.id"), primary_key=True)

    song = relationship("Song", backref="song_comments")
    comment = relationship("Comment", backref="song_comments")
