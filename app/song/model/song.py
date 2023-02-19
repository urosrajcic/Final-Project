from typing import Optional

from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Date, Float, Boolean, ForeignKey, Text
from uuid import uuid4


class Song(Base):
    __tablename__ = "song"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    length = Column(Integer, nullable=False)
    date_of_release = Column(Date, nullable=False)
    items_sold = Column(Integer, nullable=True)
    lyrics = Column(Text, nullable=True)
    ratings = Column(Float, nullable=True)
    explicit = Column(Boolean, default=False)

    genre_name = Column(String(50), ForeignKey("genre.name"), nullable=True)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(50), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")

    artists = relationship("Song", secondary="artist_song_association")

    def __init__(self, name: str,
                 length: int,
                 date_of_release: str,
                 items_sold: Optional[int] = None,
                 lyrics: Optional[str] = None,
                 ratings: Optional[float] = None,
                 explicit: Optional[bool] = False,
                 genre_name: Optional[str] = None,
                 award_id: Optional[str] = None,
                 artist: Optional[list] = []
                 ):
        self.name = name
        self.length = length
        self.date_of_release = date_of_release.strftime("%Y-%m-%d")
        self.items_sold = items_sold
        self.lyrics = lyrics
        self.ratings = ratings
        self.explicit = explicit
        self.genre_name = genre_name
        self.award_id = award_id
        self.artists = artist
