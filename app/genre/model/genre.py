from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Genre(Base):
    __tablename__ = "genre"
    name = Column(String(50), primary_key=True, autoincrement=False)

    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    song = relationship("Song", lazy="subquery")
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    artist = relationship("Artist", lazy="subquery")
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album = relationship("Album", lazy="subquery")

    def __init__(self, name, song_id=None, artist_id=None, album_id=None):
        self.name = name
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
