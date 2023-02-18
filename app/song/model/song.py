from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Date, Float, Boolean, ForeignKey
from uuid import uuid4


class Song(Base):
    __tablename__ = "song"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    length = Column(Integer)
    items_sold = Column(Integer, nullable=True)
    lyrics = Column(String(500), nullable=True)
    date_of_release = Column(Date)
    ratings = Column(Float, nullable=True)
    explicit = Column(Boolean, default=False)

    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=False)
    artist = relationship("Artist", lazy="subquery")
    genre_name = Column(String(50), ForeignKey("genre.name"), nullable=True)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(50), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")

    def __init__(self, name=name, length=length, items_sold=None, lyrics=None, date_of_release=date_of_release,
                 ratings=None, explicit=False, artist_id=artist_id, genre_name=None,
                 award_id=None):
        self.name = name
        self.length = length
        self.items_sold = items_sold
        self.lyrics = lyrics
        self.date_of_release = date_of_release
        self.ratings = ratings
        self.explicit = explicit
        self.artist_id = artist_id
        self.genre_name = genre_name
        self.award_id = award_id
