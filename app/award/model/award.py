from uuid import uuid4

from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Date, ForeignKey


class Award(Base):
    __tablename__ = "award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    award_date = Column(Date, nullable=True)

    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    song = relationship("Song", lazy="subquery")
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    artist = relationship("Artist", lazy="subquery")
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album = relationship("Artist", lazy="subquery")

    def __init__(self, name, award_date, song_id=None, artist_id=None, album_id=None):
        self.name = name
        self.award_date = award_date
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
