from app.db.database import Base
from sqlalchemy import Column, String, Date, Float, Boolean, ForeignKey
from uuid import uuid4


class Artist(Base):
    __table_name__ = "artist"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    date_of_birth = Column(Date)
    date_of_death = Column(Date, nullable=True)
    ratings = Column(Float, nullable=True)
    vocalist = Column(Boolean, default=True)
    musician = Column(Boolean, default=True)
    producer = Column(Boolean, default=True)
    writer = Column(Boolean, default=True)
    engineer = Column(Boolean, default=True)
    biography = Column(String(500), nullable=True)

    album_id = Column(String(50), ForeignKey("album.id"), nullable=True)
    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=True)
    award_id = Column(String(25), ForeignKey("award.id"), nullable=True)
    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    user_username = Column(String(50), ForeignKey("user.username"), nullable=True)
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)

    def __init__(self, name, date_of_birth=None, date_of_death=None, ratings=None, vocalist=False, musician=False,
                 producer=False, writer=False, engineer=False, biography=None, album_id=None, song_id=None,
                 genre_name=None, award_id=None, country_name=None, user_username=None, record_label_id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.ratings = ratings
        self.vocalist = vocalist
        self.musician = musician
        self.producer = producer
        self.writer = writer
        self.engineer = engineer
        self.biography = biography
        self.album_id = album_id
        self.song_id = song_id
        self.genre_name = genre_name
        self.award_id = award_id
        self.country_name = country_name
        self.user_username = user_username
        self.record_label_id = record_label_id
