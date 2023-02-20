from uuid import uuid4
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Float


class Comment(Base):
    __tablename__ = "comment"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    header = Column(String(25))
    text = Column(String(1000))
    date_time = Column(DateTime)
    ratings = Column(Float)

    user_username = Column(String(50), ForeignKey("user.username"), nullable=False)
    user = relationship("User", lazy="subquery")

    artist = relationship("Artist", secondary="artist_comments", lazy="subquery")
    album = relationship("Album", secondary="album_comments", lazy="subquery")
    song = relationship("Song", secondary="song_comments", lazy="subquery")

    def __init__(self, header: str,
                 text: str,
                 date_time: date_time,
                 user_username: str = user_username):
        self.header = header
        self.text = text
        self.date_time = date_time.datetime.now()
        self.user_username = user_username
