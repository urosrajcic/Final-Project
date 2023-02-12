from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey


class Genre(Base):
    __table_name__ = "genre"
    name = Column(String(50), primary_key=True, autoincrement=False)

    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)

    def __init__(self, name, song_id=None, artist_id=None, album_id=None):
        self.name = name
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
