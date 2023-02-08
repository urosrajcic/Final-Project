from uuid import uuid4
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer


class Comment(Base):
    __table_name__ = "comment"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    header = Column(String(25))
    text = Column(String(1000))
    datetime = Column(DateTime)
    ratings = Column(Integer)

    user_username = Column(String(50), ForeignKey("user.username"), nullable=False)
    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)

    def __init__(self, header, text, datetime, ratings, user_username, song_id,
                 artist_id, album_id, record_label_id):
        self.header = header
        self.text = text
        self.datetime = datetime
        self.ratings = ratings
        self.user_username = user_username
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
        self.record_label_id = record_label_id
