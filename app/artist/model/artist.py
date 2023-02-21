from uuid import uuid4

from sqlalchemy import Column, String, Date, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Artist(Base):
    __tablename__ = "artist"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    date_of_birth = Column(Date, nullable=True)
    date_of_death = Column(Date, nullable=True)
    ratings = Column(Float, nullable=True)
    vocalist = Column(Boolean, default=False, nullable=True)
    musician = Column(Boolean, default=False, nullable=True)
    producer = Column(Boolean, default=False, nullable=True)
    writer = Column(Boolean, default=False, nullable=True)
    engineer = Column(Boolean, default=False, nullable=True)
    biography = Column(Text, nullable=True)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    country = relationship("Country", lazy="subquery")
    record_label_id = Column(String(25), ForeignKey("record_label.id"), nullable=True)
    record_label = relationship("RecordLabel", lazy="subquery")

    songs = relationship("Song", secondary="artist_song_association", lazy="subquery")
    albums = relationship("Album", secondary="artist_album_association", lazy="subquery")
    comments = relationship("Comment", secondary="artist_comments", lazy="subquery")
    awards = relationship("Award", secondary="artist_awards", lazy="subquery")
    genres = relationship("Genre", secondary="artist_genres", lazy="subquery")

    def __init__(self, name: str,
                 country_name: str,
                 date_of_birth: str,
                 ratings: float = None
                 ):
        self.name = name
        self.country_name = country_name
        self.date_of_birth = date_of_birth.strftime("%Y-%m-%d")
        self.ratings = ratings
