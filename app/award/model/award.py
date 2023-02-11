from app.db.database import Base
from sqlalchemy import Column, String, Date, ForeignKey


class Award(Base):
    __table_name__ = "award"
    name = Column(String(50), primary_key=True, autoincrement=False)
    award_date = Column(Date, nullable=True)

    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)

    def __init__(self, name, award_date, song_id, artist_id, album_id):
        self.name = name
        self.award_date = award_date
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
