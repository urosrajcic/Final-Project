from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class AlbumGenres(Base):
    __tablename__ = "album_genres"

    album_id = Column(String(50), ForeignKey("album.id"), primary_key=True)
    genre_name = Column(String(50), ForeignKey("genre.name"), primary_key=True)

    album = relationship("Album", backref="album_genres")
    genre = relationship("Genre", backref="album_genres")
