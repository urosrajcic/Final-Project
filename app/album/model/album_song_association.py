from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class AlbumSongAssociation(Base):
    __tablename__ = "album_song_association"

    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)
    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)

    album = relationship("Album", backref="album_song_association")
    song = relationship("Song", backref="album_song_association")
