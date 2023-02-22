from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class ArtistAlbumAssociation(Base):
    __tablename__ = "artist_album_association"

    artist_id = Column(String(50), ForeignKey("artist.id"), primary_key=True)
    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)

    artist = relationship("Artist", backref="artist_album_association")
    album = relationship("Album", backref="artist_album_association")
