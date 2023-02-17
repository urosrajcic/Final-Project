from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Boolean, Date, ForeignKey


class User(Base):
    __tablename__ = "user"
    username = Column(String(50), primary_key=True, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(25))
    surname = Column(String(25))
    date_of_birth = Column(Date)
    critic = Column(Boolean, default=False)
    writer = Column(Boolean, default=False)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    country = relationship("Country", lazy="subquery")
    song_id = Column(String(50), ForeignKey("song.id"), nullable=True)
    song = relationship("Song", lazy="subquery")
    artist_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    artist = relationship("Artist", lazy="subquery")
    album_id = Column(String(50), ForeignKey("artist.id"), nullable=True)
    album = relationship("Album", lazy="subquery")

    def __init__(self, username, email, password, name, surname, date_of_birth, critic=False, writer=False,
                 country_name=country_name, song_id=None, artist_id=None, album_id=None):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.critic = critic
        self.writer = writer
        self.country_name = country_name
        self.song_id = song_id
        self.artist_id = artist_id
        self.album_id = album_id
