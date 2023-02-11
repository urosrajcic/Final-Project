from app.db.database import Base
from sqlalchemy import Column, String, Integer, Date, Float, Boolean, ForeignKey
from uuid import uuid4


class Song(Base):
    __table_name__ = "song"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    length = Column(Integer)
    items_sold = Column(Integer, nullable=True)
    lyrics = Column(String(500), nullable=True)
    date_of_release = Column(Date)
    ratings = Column(Float, nullable=True)
    explicit = Column(Boolean, default=False)

    album_id = Column(String(50), ForeignKey("artist.id"), nullable=False)
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=False)
    genre_name = Column(String(50), ForeignKey("genre.name"), nullable=False)
    award_id = Column(String(50), ForeignKey("award.name"), nullable=True)
    user_username = Column(String(50), ForeignKey("user.username"), nullable=True)
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)

    def __init__(self, name, length, items_sold, lyrics, date_of_release, ratings, explicit,
                 album_id, artis_id, genre_name, award_name, user_username, record_label_id):
        self.name = name
        self.length = length
        self.items_sold = items_sold
        self.lyrics = lyrics
        self.date_of_release = date_of_release
        self.ratings = ratings
        self.explicit = explicit
        self.album_id = album_id
        self.artist_id = artis_id
        self.genre_name = genre_name
        self.award_name = award_name
        self.user_username = user_username
        self.record_label_id = record_label_id
