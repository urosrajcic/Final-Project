from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupAlbumAssociation(Base):
    __tablename__ = "group_album_association"

    group_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)

    group = relationship("Group", backref="group_album_association")
    album = relationship("Album", backref="group_album_association")
