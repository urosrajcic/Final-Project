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

    album_id = Column(String(50), ForeignKey("album.id"), nullable=False)
    song_id = Column(String(50), ForeignKey("song.id"), nullable=False)
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=False)
    award_name = Column(String(25), ForeignKey("award.name"), nullable=True)
    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    user_username = Column(String(50), ForeignKey("user.username"), nullable=True)
    record_label_id = Column(String(50), ForeignKey("record_label.id"), nullable=True)

    def __init__(self, name, date_of_birth, date_of_death, ratings, vocalist, musician, producer, writer, engineer,
                 biography, album_id, song_id, genre_name, award_name, country_name, user_username, record_label_id):
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
        self.award_name = award_name
        self.country_name = country_name
        self.user_username = user_username
        self.record_label_id = record_label_id
