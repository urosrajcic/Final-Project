from app.db.database import Base
from sqlalchemy import Column, String, Integer, Date, Float, Boolean, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


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

    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=True)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(25), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")

    artists = relationship("Artist", secondary="artist_album_association", lazy="subquery")
    songs = relationship("Song", secondary="album_song_association", lazy="subquery")
    comments = relationship("Comment", secondary="album_comments", lazy="subquery")

    def __init__(self, name: str,
                 length: int,
                 date_of_release: str,
                 ):
        self.name = name
        self.length = length
        self.date_of_release = date_of_release.strftime("%Y-%m-%d")
