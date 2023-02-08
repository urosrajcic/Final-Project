from app.db.database import Base
from sqlalchemy import Column, String, Integer, Date, Float, Boolean, ForeignKey
from uuid import uuid4


class Album(Base):
    __table_name__ = "album"

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
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=False)
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=False)
    award_name = Column(String(25), ForeignKey("award.name"), nullable=True)
    user_username = Column(String(50), ForeignKey("user.username"), nullable=True)
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)

    def __init__(self, name, length, date_of_release, items_sold, ratings, explicit, lp, ep, single, mixtape,
                 song_id, artis_id, genre_name, award_name, user_username, record_label_id):
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
        self.award_name = award_name
        self.user_username = user_username
        self.record_label_id = record_label_id
