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

    artists = relationship("Artist", secondary="artist_song_association", lazy="subquery")
    albums = relationship("Album", secondary="album_song_association", lazy="subquery")
    comments = relationship("Comment", secondary="song_comments", lazy="subquery")
    awards = relationship("Award", secondary="song_awards", lazy="subquery")
    genres = relationship("Genre", secondary="song_genres", lazy="subquery")

    def __init__(self, name: str,
                 length: int,
                 date_of_release: str,
                 ):
        self.name = name
        self.length = length
        self.date_of_release = date_of_release.strftime("%Y-%m-%d")
