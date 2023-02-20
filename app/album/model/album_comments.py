from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class AlbumComments(Base):
    __tablename__ = "album_comments"

    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)
    comment_id = Column(String(50), ForeignKey("comment.id"), primary_key=True)

    album = relationship("Album", backref="album_comments")
    comment = relationship("Comment", backref="album_comments")
