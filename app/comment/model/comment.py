from typing import Optional
from uuid import uuid4
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Float
from datetime import datetime


class Comment(Base):
    __tablename__ = "comment"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    header = Column(String(25))
    text = Column(String(1000))
    date_time = Column(DateTime)
    ratings = Column(Float)

    user_username = Column(String(50), ForeignKey("user.username"), nullable=False)
    user = relationship("User", lazy="subquery")
    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    song = relationship("Song", lazy="subquery")
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    artist = relationship("Artist", lazy="subquery")
    album_id = Column(String(50), ForeignKey("album.id"), nullable=True)
    album = relationship("Album", lazy="subquery")
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)
    record_label = relationship("RecordLabel", lazy="subquery")

    def __init__(self, header: str,
                 text: str,
                 date_time: date_time,
                 ratings: Optional[float] = None,
                 user_username: str = user_username,
                 song_id: Optional[str] = None,
                 artist_id: Optional[str] = None,
                 album_id: Optional[str] = None,
                 record_label_id: Optional[str] = None):
        self.header = header
        self.text = text
        self.date_time = datetime.now()
        self.ratings = ratings
        self.user_username = user_username
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
        self.record_label_id = record_label_id
