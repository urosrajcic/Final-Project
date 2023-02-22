from uuid import uuid4

from sqlalchemy import Column, String, Integer, Date, Float, Boolean
from sqlalchemy.orm import relationship

from app.db import Base


class Album(Base):
    __tablename__ = "album"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    length = Column(Integer)
    date_of_release = Column(Date)
    items_sold = Column(Integer, nullable=True)
    ratings = Column(Float, nullable=True)
    explicit = Column(Boolean, default=False)
    lp = Column(Boolean, default=False)
    ep = Column(Boolean, default=False)
    single = Column(Boolean, default=False)
    mixtape = Column(Boolean, default=False)

    artists = relationship("Artist", secondary="artist_album_association", lazy="subquery")
    songs = relationship("Song", secondary="album_song_association", lazy="subquery")
    comments = relationship("Comment", secondary="album_comments", lazy="subquery")
    awards = relationship("Award", secondary="album_awards", lazy="subquery")
    genres = relationship("Genre", secondary="album_genres", lazy="subquery")
    
    def __init__(self, name: str,
                 length: int,
                 date_of_release: str,
                 ratings: float = None
                 ):
        self.name = name
        self.length = length
        self.date_of_release = date_of_release.strftime("%Y-%m-%d")
        self.ratings = ratings
