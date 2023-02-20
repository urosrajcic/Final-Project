from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class ArtistGenres(Base):
    __tablename__ = "artist_genres"

    artist_id = Column(String(50), ForeignKey("artist.id"), primary_key=True)
    genre_name = Column(String(50), ForeignKey("genre.name"), primary_key=True)

    artist = relationship("Artist", backref="artist_genres")
    genre = relationship("Genre", backref="artist_genres")
