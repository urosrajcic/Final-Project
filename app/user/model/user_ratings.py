from uuid import uuid4

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer, UniqueConstraint


class UserRating(Base):
    __tablename__ = "user_ratings"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    user_username = Column(String(50), ForeignKey("user.username"))
    album_id = Column(String(50), ForeignKey("album.id"))
    artist_id = Column(String(50), ForeignKey("artist.id"))
    song_id = Column(String(50), ForeignKey("song.id"))
    rating = Column(Integer)

    __table_args__ = (UniqueConstraint("user_username", "album_id", name="album_user_rating_uc"),
                      UniqueConstraint("user_username", "artist_id", name="artist_user_rating_uc"),
                      UniqueConstraint("user_username", "song_id", name="song_user_rating_uc"))

    def __init__(self, user_username: str,
                 rating: int,
                 album_id: str = None,
                 artist_id: str = None,
                 song_id: str = None):
        self.user_username = user_username
        self.rating = rating
        self.album_id = album_id
        self.artist_id = artist_id
        self.song_id = song_id
