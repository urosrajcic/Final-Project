from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class SongGenres(Base):
    __tablename__ = "song_genres"

    song_id = Column(String(50), ForeignKey("song.id"), primary_key=True)
    genre_name = Column(String(50), ForeignKey("genre.name"), primary_key=True)

    song = relationship("Song", backref="song_genres")
    genre = relationship("Genre", backref="song_genres")
