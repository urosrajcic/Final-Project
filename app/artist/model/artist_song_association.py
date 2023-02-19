from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class ArtistSongAssociation(Base):
    __tablename__ = "artist_song_association"

    artist_id = Column(String(50), ForeignKey("artist.id"), primary_key=True)
    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)

    artist = relationship("Artist", backref="artist_song_association")
    song = relationship("Song", backref="artist_song_association")
