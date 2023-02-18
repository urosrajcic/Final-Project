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

    song_id = Column(String(50), ForeignKey("song.id"), nullable=False)
    song = relationship("Song", lazy="subquery")
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=False)
    artist = relationship("Artist", lazy="subquery")
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=False)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(25), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")

    def __init__(self, name=name, length=None, date_of_release=date_of_release, items_sold=None, ratings=None,
                 explicit=False, lp=False, ep=False, single=False, mixtape=False, song_id=song_id, artis_id=artist_id,
                 genre_name=None, award_id=None):
        self.name = name
        self.length = length
        self.date_of_release = date_of_release
        self.items_sold = items_sold
        self.ratings = ratings
        self.explicit = explicit
        self.lp = lp
        self.ep = ep
        self.single = single
        self.mixtape = mixtape
        self.song_id = song_id
        self.artist_id = artis_id
        self.genre_name = genre_name
        self.award_id = award_id
